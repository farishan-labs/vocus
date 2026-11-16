# Proposal

## Why

mdview bundles a GTK3+WebKit viewer with markdown-specific rendering, so its
fullscreen/Esc-close/search/TOC shell cannot be reused by other viewers (e.g.
flowview). Extracting that shell into a tiny, dumb, fast, extensible "vocus"
(view focus) frame lets mdview and future viewers depend on it instead of
duplicating native window code.

## What Changes

- New project `vocus`: a minimal native viewer (GTK3 + WebKit2GTK) that renders
  arbitrary HTML passed on stdin or via `--html <file>`, with fullscreen,
  borderless window, Esc to close, and auto light/dark theming.
- Intentionally dumb frame: no markdown, Mermaid, or TOC logic; content brings
  its own.
- mdview refactored to depend on vocus: renders Markdown to HTML, pipes it to
  vocus. (Separate change in mdview repo.)
- Optional local cache of `pele.global.js` not in scope here (flowview's concern).

## Capabilities

### New Capabilities
- `native-viewer-frame`: render arbitrary HTML in a fullscreen, borderless,
  Esc-closable native GTK/WebKit window with auto theming.

### Modified Capabilities
- (none)

## Impact

- New repo `~/dev/labs/vocus` (Python, GTK3 + WebKit2GTK).
- mdview repo: dependency on vocus; future flowview depends on vocus.
- No breaking changes to mdview CLI surface (it keeps resolving files/dirs/slugs).