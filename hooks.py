"""Build hooks for the Muse transcripts section.

Dropping a new .html file into docs/models/muse/transcripts/assets/ is
enough: at build time this hook generates one wrapper page per transcript
(models/muse/transcripts/<stem>/index.md) embedding the asset in an
iframe, with webcomic-style Prev / Index / Next navigation on top, and
fills the transcripts index page's placeholder with a newest-first list
of links. Standard library only.
"""

import os
import tempfile

from mkdocs.structure.files import File

SECTION_DIR = os.path.join("models", "muse", "transcripts")
ASSETS_SUBDIR = "assets"
INDEX_SRC = os.path.join(SECTION_DIR, "index.md")
PLACEHOLDER = "<!-- TRANSCRIPTS -->"

_gen_dir = None


def _label(stem):
    """'2026-10-14-keys' -> '2026-10-14 keys' (date keeps its dashes)."""
    parts = stem.split("-", 3)
    if len(parts) == 4 and all(p.isdigit() for p in parts[:3]):
        return "-".join(parts[:3]) + " " + parts[3].replace("-", " ")
    return stem.replace("-", " ")


def _entries(config):
    """[(stem, filename, label)] for assets/*.html, filename ascending."""
    assets_dir = os.path.join(config["docs_dir"], SECTION_DIR, ASSETS_SUBDIR)
    entries = []
    if os.path.isdir(assets_dir):
        for name in sorted(os.listdir(assets_dir)):
            if name.lower().endswith(".html"):
                stem = name[: -len(".html")]
                entries.append((stem, name, _label(stem)))
    return entries


def _wrapper_md(entries, i):
    stem, filename, label = entries[i]
    if i > 0:
        prev_cell = f'<a href="../{entries[i - 1][0]}/">&larr; Prev</a>'
    else:
        prev_cell = '<span style="color:#9a9aa0;">&larr; Prev</span>'
    if i < len(entries) - 1:
        next_cell = f'<a href="../{entries[i + 1][0]}/">Next &rarr;</a>'
    else:
        next_cell = '<span style="color:#9a9aa0;">Next &rarr;</span>'
    nav = (
        '<div style="display:flex;justify-content:space-between;'
        'align-items:center;max-width:640px;margin:0 auto 16px;">'
        f"<span>{prev_cell}</span>"
        '<a href="../"><strong>Index</strong></a>'
        f"<span>{next_cell}</span>"
        "</div>"
    )
    iframe = (
        f'<iframe src="../assets/{filename}" '
        'style="width:100%;border:0;display:block;" '
        "onload=\"this.style.height = "
        "this.contentWindow.document.documentElement.scrollHeight + 'px'\"></iframe>"
    )
    return f"# {label}\n\n{nav}\n\n{iframe}\n"


def on_files(files, config):
    global _gen_dir
    entries = _entries(config)
    if not entries:
        return files
    _gen_dir = tempfile.mkdtemp(prefix="transcripts-gen-")
    for i, entry in enumerate(entries):
        rel = os.path.join(SECTION_DIR, entry[0], "index.md")
        dest = os.path.join(_gen_dir, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(_wrapper_md(entries, i))
        files.append(
            File(
                path=rel,
                src_dir=_gen_dir,
                dest_dir=config["site_dir"],
                use_directory_urls=True,
            )
        )
    return files


def on_page_markdown(markdown, page, config, files):
    if page.file.src_path != INDEX_SRC or PLACEHOLDER not in markdown:
        return markdown
    entries = _entries(config)
    listing = "\n".join(
        f"- [{label}]({stem}/)" for stem, _name, label in reversed(entries)
    )
    return markdown.replace(PLACEHOLDER, listing)
