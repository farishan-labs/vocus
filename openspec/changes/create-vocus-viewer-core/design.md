# Design

## Context

mdview currently couples Markdown rendering with a GTK3+WebKit native window shell.
The shell (fullscreen, Esc close, search, theming) is reusable but not separable.
vocus extracts only the dumb frame; mdview becomes a content producer.

## Goals / Non-Goals

**Goals:**
- Tiny, fast, minimal native HTML frame.
- Read HTML from stdin or `--html <file>`.
- Fullscreen borderless, Esc close, auto light/dark theme, optional `--title`.

**Non-Goals:**
- No Markdown/Mermaid parsing, TOC, or search logic (content's job).
- No theming knobs beyond system preference.
- No network fetching; content is supplied locally.

## Decisions

- **Python + GTK3 + WebKit2GTK 4.0**: matches mdview's existing stack; no new
  system deps; reuse install-deps pattern.
- **stdin-first input**: `vocus` with no args reads stdin; `--html` reads file.
  Enables composition: `mdview` pipes rendered HTML.
- **No TOC/search in core**: keeps frame dumb and fast; mdview can inject its
  own JS for those features into the HTML it produces.
- **Packaging**: pyproject + console script `vocus`; pip editable install.

## Risks / Trade-offs

- WebKit2GTK version availability (4.0 vs 4.1) on newer distros → mitigation:
  prefer 4.1 with fallback import.
- Larger HTML payloads on stdin → mitigation: read fully before showing window.

## Migration Plan

1. Scaffold vocus repo + CLI + window.
2. Publish/install vocus on PATH.
3. Refactor mdview to render HTML and pipe to vocus (separate change).