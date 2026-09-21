"""Verify sites.js and the folder agree: every entry points at a real file,
and every .html page (other than index.html) is listed. Exit 1 on mismatch."""
import pathlib, re, sys

root = pathlib.Path(__file__).parent
listed = re.findall(r'file:\s*"([^"]+)"', (root / "sites.js").read_text(encoding="utf-8"))
pages = {p.name for p in root.glob("*.html")} - {"index.html"}

missing = [f for f in listed if not (root / f).is_file()]
unlisted = sorted(pages - set(listed))
dupes = sorted({f for f in listed if listed.count(f) > 1})

for label, items in (("Listed but no file", missing), ("File not listed", unlisted), ("Listed twice", dupes)):
    for f in items:
        print(f"{label}: {f}")
print(f"{len(listed)} entries, {len(pages)} pages")
sys.exit(1 if missing or unlisted or dupes else 0)
