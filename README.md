# vocus

Tiny, fast, minimal, extensible native HTML viewer for Linux (GTK3 + WebKit2GTK).

vocus is a **dumb frame**: it renders supplied HTML as-is. No Markdown, no
Mermaid, no TOC/search logic. Content producers (mdview, flowview, ...) render
their own HTML and pipe it in.

## Requirements

- Ubuntu 22.04+ (X11)
- Python 3.10+
- GTK 3 + WebKit2GTK 4.0

Install deps:

```bash
./install-deps.sh
```

## Install

```bash
pip install -e .
```

## Usage

```bash
echo '<h1>hello</h1>' | vocus
vocus --html report.html --title "Report"
```

Keyboard: `Esc` closes the window. Fullscreen, borderless. Auto light/dark
theme based on system preference.

## License

GPL-3.0 (consistent with mdview).