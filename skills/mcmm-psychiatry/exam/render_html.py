#!/usr/bin/env python3
"""Render psychiatric_status.md → psychiatric_status.html with embedded CSS.

Self-contained, opens via file:// without external assets.
"""

from pathlib import Path
import markdown

HERE = Path(__file__).resolve().parent
MD_PATH = HERE / "psychiatric_status.md"
HTML_PATH = HERE / "psychiatric_status.html"

CSS = """
:root {
  --bg: #fafaf7;
  --text: #1a1a1a;
  --muted: #555;
  --rule: #d8d4c5;
  --psych: #2c5282;
  --h3: #4a5568;
  --gold: #b08d57;
  --code-bg: #f0eee5;
  --quote-bg: #fbf8ee;
}

* { box-sizing: border-box; }

html, body {
  background: var(--bg);
  color: var(--text);
  margin: 0;
  padding: 0;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, sans-serif;
  font-size: 17px;
  line-height: 1.7;
  max-width: 760px;
  margin: 40px auto;
  padding: 0 24px 80px;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
}

h1, h2, h3, h4 {
  font-family: Georgia, "Iowan Old Style", "Charter", serif;
  font-weight: 700;
  line-height: 1.25;
}

h1 {
  font-size: 32px;
  margin: 0 0 24px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--rule);
}

h2 {
  font-size: 24px;
  color: var(--psych);
  margin: 40px 0 12px;
  padding-bottom: 6px;
  border-bottom: 1px solid var(--rule);
}

h3 {
  font-size: 19px;
  color: var(--h3);
  margin: 28px 0 8px;
}

h4 {
  font-size: 17px;
  color: var(--h3);
  margin: 20px 0 6px;
}

p { margin: 0 0 14px; }

a { color: var(--psych); text-decoration: underline; }

ul, ol { padding-left: 22px; margin: 0 0 16px; }
li { margin-bottom: 6px; }

blockquote {
  border-left: 3px solid var(--psych);
  background: var(--quote-bg);
  padding: 10px 16px;
  margin: 16px 0;
  color: var(--muted);
  font-style: italic;
}

blockquote p { margin: 6px 0; }

code {
  background: var(--code-bg);
  padding: 2px 6px;
  border-radius: 3px;
  font-family: "SF Mono", Menlo, Monaco, "Roboto Mono", monospace;
  font-size: 0.92em;
}

pre {
  background: var(--code-bg);
  padding: 14px 16px;
  border-radius: 6px;
  overflow-x: auto;
  font-size: 0.92em;
  line-height: 1.5;
}

pre code {
  background: transparent;
  padding: 0;
  font-size: inherit;
}

hr {
  border: 0;
  border-top: 1px solid var(--rule);
  margin: 36px 0;
}

table {
  border-collapse: collapse;
  width: 100%;
  margin: 16px 0;
  font-size: 0.95em;
}

th, td {
  border: 1px solid var(--rule);
  padding: 8px 12px;
  text-align: left;
  vertical-align: top;
}

th {
  background: var(--code-bg);
  font-weight: 600;
}

strong { font-weight: 700; }

em {
  font-style: italic;
  color: var(--muted);
}

/* Cross-references: jointly em + strong → gold accent + bold */
em strong, strong em {
  color: var(--gold);
  font-weight: 700;
  font-style: italic;
}

/* Standalone em immediately after a long-dash inside paragraphs (cross-ref pattern) */
p > em:only-child {
  display: block;
  margin-top: 8px;
  font-size: 0.95em;
  color: var(--gold);
  font-weight: 600;
}

@media print {
  body {
    background: white;
    color: black;
    max-width: none;
    margin: 0;
    padding: 0 12mm;
    font-size: 12pt;
    line-height: 1.5;
  }
  h1, h2, h3, h4 { color: black; page-break-after: avoid; }
  blockquote { background: white; color: #333; }
  pre, code { background: #f5f5f5; }
  hr { page-break-after: always; border: 0; }
  a { color: black; text-decoration: none; }
}
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Психічний статус пацієнтки — MCMM екзамен</title>
<style>{css}</style>
</head>
<body>
{body}
</body>
</html>
"""


def main() -> None:
    md_text = MD_PATH.read_text(encoding="utf-8")

    html_body = markdown.markdown(
        md_text,
        extensions=[
            "extra",  # tables, footnotes, fenced_code, abbr, attr_list, def_list
            "sane_lists",
            "smarty",
            "toc",
        ],
        output_format="html5",
    )

    html = HTML_TEMPLATE.format(css=CSS.strip(), body=html_body)
    HTML_PATH.write_text(html, encoding="utf-8")
    print(f"Wrote {HTML_PATH} ({HTML_PATH.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
