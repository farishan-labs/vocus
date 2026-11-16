# Spec Delta

## Purpose

A minimal native frame that renders arbitrary HTML in a fullscreen, borderless,
Esc-closable window, so markdown/flow viewers can reuse the shell without
duplicating GTK/WebKit code.

## ADDED Requirements

### Requirement: Render HTML from stdin or file
The system SHALL render HTML supplied via stdin or the `--html <path>` option
and display it in a native window.

#### Scenario: HTML from stdin
- **WHEN** HTML is piped to stdin
- **THEN** the window displays the rendered HTML

#### Scenario: HTML from file
- **WHEN** `--html report.html` is passed
- **THEN** the window displays the contents of that file

### Requirement: Fullscreen borderless window
The system SHALL open in fullscreen borderless mode by default.

#### Scenario: Launch shows fullscreen
- **WHEN** the viewer starts
- **THEN** the window is fullscreen and borderless

### Requirement: Esc closes the window
The system SHALL close the window when the user presses Esc.

#### Scenario: Esc closes
- **WHEN** the window is focused and the user presses Esc
- **THEN** the window closes

### Requirement: Auto light/dark theming
The system SHALL apply a theme matching the system preference (light or dark).

#### Scenario: Dark preference
- **WHEN** the system is in dark mode
- **THEN** the window uses the dark theme

### Requirement: Optional title
The system SHALL accept an optional `--title` to set the window title.

#### Scenario: Title set
- **WHEN** `--title "Flow"` is passed
- **THEN** the window title is "Flow"

### Requirement: No content knowledge
The system SHALL NOT parse, transform, or interpret the supplied HTML; it
renders it as-is.

#### Scenario: Raw HTML passthrough
- **WHEN** arbitrary HTML with scripts is supplied
- **THEN** it is rendered without modification by the frame