# vocus

Tiny, fast, minimal, extensible native HTML viewer for Linux (GTK3 + WebKit2GTK).

vocus is a **dumb frame**: it renders supplied HTML as-is. No Markdown, no
Mermaid, no TOC/search logic. Content producers (mdview, flowview, ...) render
their own HTML and pipe it in.

## Requirements

- Tested on Ubuntu 22.04+ (X11). Other distros may work; if you need help,
  open an issue at https://github.com/farishan-labs/vocus/issues.
- Python 3.10+
- GTK 3 + WebKit2GTK 4.0

Install deps:

```bash
./install-deps.sh
```

## Install

```bash
curl -fsSL https://farishan-labs.github.io/vocus/install.sh | bash
```

## Usage

```bash
echo '<h1>hello</h1>' | vocus
vocus --html report.html --title "Report"
```

Keyboard: `Esc` closes the window. Fullscreen, borderless. Auto light/dark
theme based on system preference.

## Used by

- [mdview](https://github.com/farishan-labs/mdview) — native Markdown viewer (renders Markdown to HTML, pipes to vocus).
- flowview (planned) — Mermaid/flow viewer (Pele → HTML, pipes to vocus).

## License

GPL-3.0 (consistent with mdview).