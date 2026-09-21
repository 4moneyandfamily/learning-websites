# Learning Websites

Static site on GitHub Pages. Repo: `4moneyandfamily/learning-websites`, branch `main`, served from the root.

- `index.html` is the landing page. It renders cards from `sites.js`; do not hardcode cards in the HTML.
- Each learning site is one standalone `.html` file in this folder.

## Adding sites

1. Put the new `.html` file(s) in this folder. Keep filenames lowercase-with-hyphens, no spaces.
2. Add one entry per file to `window.SITES` in `sites.js` (`file`, `title`, `blurb`, `topic`, `added`). Pull title and blurb from the page's `<title>` and hero text.
3. Run `python check.py`. It must exit 0.
4. Commit and push to `main`. Pages redeploys in about a minute.
