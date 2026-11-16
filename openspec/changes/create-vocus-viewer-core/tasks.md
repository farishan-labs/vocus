# Tasks

## 1. Scaffold

- [x] 1.1 Create repo layout (pyproject.toml, vocus/__init__.py, vocus/cli.py, vocus/window.py) and verify files exist
- [x] 1.2 Add install-deps.sh (python3, libgtk-3-dev, libwebkit2gtk-4.0-dev) and verify runs clean

## 2. Core frame

- [x] 2.1 Implement GTK window: fullscreen, borderless, Esc close; verify launches and closes with Esc
- [x] 2.2 Implement WebKit view loading HTML from stdin or --html; verify renders supplied HTML
- [x] 2.3 Implement --title option; verify window title set
- [x] 2.4 Implement auto light/dark theme via prefers-color-scheme; verify both themes apply
- [x] 2.5 Ensure HTML passthrough (no transformation); verify scripts/styles preserved

## 3. CLI & packaging

- [x] 3.1 Add argparse CLI (stdin/--html/--title) with usage help; verify `vocus --help`
- [x] 3.2 Add pyproject console script `vocus`; verify `pip install -e .` then `vocus` on PATH
- [x] 3.3 Add README.md with usage and verify example commands run

## 4. Integration

- [x] 4.1 Verify `echo '<h1>hi</h1>' | vocus` opens and closes with Esc
- [x] 4.2 Verify `vocus --html sample.html` opens supplied file

## Workflow follow-up

- Archive the change after review.
- Refactor mdview to depend on vocus (separate change).