"""Native window shell for vocus."""

import subprocess
import sys

import gi

gi.require_version("WebKit2", "4.0")
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")

from gi.repository import Gdk, Gtk, WebKit2


def _is_dark() -> bool:
    try:
        out = subprocess.check_output(
            ["gsettings", "get", "org.gnome.desktop.interface", "color-scheme"],
            stderr=subprocess.DEVNULL, text=True,
        ).strip().lower()
        if "dark" in out:
            return True
        if "light" in out:
            return False
    except Exception:
        pass
    try:
        out = subprocess.check_output(
            ["gsettings", "get", "org.gnome.desktop.interface", "gtk-theme"],
            stderr=subprocess.DEVNULL, text=True,
        ).strip().lower()
        if "dark" in out:
            return True
    except Exception:
        pass
    return False


class VocusWindow(Gtk.Window):
    def __init__(self, html: str, title: str = "vocus"):
        super().__init__(title=title)
        self.set_decorated(False)
        self.fullscreen()

        dark = _is_dark()
        bg = "#1e1e2e" if dark else "#fafafa"
        self.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(*_rgba(bg)))

        webview = WebKit2.WebView()
        webview.load_html(html, "file:///")
        self.add(webview)

        self.connect("key-press-event", self._on_key)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def _on_key(self, widget, event):
        if event.keyval == Gdk.KEY_Escape:
            self.destroy()
            return True
        return False


def _rgba(hexcolor: str):
    hexcolor = hexcolor.lstrip("#")
    r = int(hexcolor[0:2], 16) / 255.0
    g = int(hexcolor[2:4], 16) / 255.0
    b = int(hexcolor[4:6], 16) / 255.0
    return (r, g, b, 1.0)


def run(html: str, title: str = "vocus") -> None:
    VocusWindow(html, title=title)
    Gtk.main()