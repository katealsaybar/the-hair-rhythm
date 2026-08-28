#!/usr/bin/env python3
"""Port this standalone page into the tara-rose-pages tree. One direction only.

This folder is the readable source. The tree copy at
../tara-rose-pages-main/the-hair-rhythm/index.html is GENERATED from it by this
script, so the two can never drift silently again (they did twice by hand).

    python port.py            # regenerate the tree copy, then run build.py there

What it does, in order:
 1. index.html: fonts.css link becomes the inline @font-face preamble with tree
    font paths; the three stylesheet links collapse to the build.py marker; every
    assets/img/ path becomes /tara-rose-pages/assets/; every js/ script tag is
    inlined.
 2. css/the-hair-rhythm.css is synced to _css/page-the-hair-rhythm.css with the
    first-line name adjusted. trs-core.css and trs-blocks.css are shared: they are
    verified against _css (trs-blocks.css is _css/page-beauty-voucher.css) and the
    port REFUSES if they differ, because a shared-sheet edit belongs in _css first.
 3. Images in assets/img/ are copied into the tree's shared assets/.
 4. docs/BUILD-NOTES.md is copied beside the tree page.
 5. build.py runs in the tree, then build.py --check.
"""
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TREE = os.path.normpath(os.path.join(HERE, "..", "tara-rose-pages-main"))
DST = os.path.join(TREE, "the-hair-rhythm")
BASE = "/tara-rose-pages"


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def write(p, text):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    # 2 first, so a shared-sheet drift stops the port before anything is written.
    pairs = [
        ("css/trs-core.css", "_css/trs-core.css"),
        ("css/trs-blocks.css", "_css/page-beauty-voucher.css"),
    ]
    for src, dst in pairs:
        if read(os.path.join(HERE, src)) != read(os.path.join(TREE, dst)):
            sys.exit(f"refusing: {src} differs from {dst} — fix the shared sheet in _css first, then re-copy it here")

    page_css = read(os.path.join(HERE, "css", "the-hair-rhythm.css"))
    page_css = page_css.replace("/* the-hair-rhythm.css.", "/* page-the-hair-rhythm.css.", 1)
    write(os.path.join(TREE, "_css", "page-the-hair-rhythm.css"), page_css)

    # 1. The page itself.
    html = read(os.path.join(HERE, "index.html"))

    fonts = read(os.path.join(HERE, "css", "fonts.css")).strip()
    fonts = fonts.replace("url(../assets/fonts/", f"url({BASE}/assets/fonts/")
    html = html.replace('<link rel="stylesheet" href="css/fonts.css">', f"<style>{fonts}</style>")

    html = html.replace('<link rel="stylesheet" href="css/trs-core.css">', "<!-- trs:css -->")
    html = html.replace('\n<link rel="stylesheet" href="css/trs-blocks.css">', "")
    html = html.replace('\n<link rel="stylesheet" href="css/the-hair-rhythm.css">', "")

    html = html.replace('href="assets/fonts/', f'href="{BASE}/assets/fonts/')
    html = html.replace("assets/img/", f"{BASE}/assets/")

    def inline(m):
        return "<script>\n" + read(os.path.join(HERE, "js", m.group(1))).strip() + "\n</script>"

    html = re.sub(r'<script src="js/([\w.-]+)" defer></script>', inline, html)

    os.makedirs(DST, exist_ok=True)
    write(os.path.join(DST, "index.html"), html)

    # 3. Images.
    imgdir = os.path.join(HERE, "assets", "img")
    for name in sorted(os.listdir(imgdir)):
        shutil.copyfile(os.path.join(imgdir, name), os.path.join(TREE, "assets", name))

    # 4. The notes travel with the page.
    shutil.copyfile(os.path.join(HERE, "docs", "BUILD-NOTES.md"), os.path.join(DST, "BUILD-NOTES.md"))

    # 5. Inline the CSS, then prove the tree is consistent.
    for args in (["python", "build.py"], ["python", "build.py", "--check"]):
        r = subprocess.run(args, cwd=TREE)
        if r.returncode:
            sys.exit(r.returncode)
    print("ported: the tree copy is regenerated from this folder")


if __name__ == "__main__":
    main()
