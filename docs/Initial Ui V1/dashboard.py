#!/usr/bin/env python3
# Omega_BSD - Initial Dashboard
# 6-tile launcher, console-style

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
import subprocess

TILES = [
    ("Firefox", ["firefox"]),
    ("Files", ["pcmanfm"]),
    ("Terminal", ["xterm"]),
    ("Empty", None),
    ("Empty", None),
    ("Empty", None),
]

class Dashboard(Gtk.Window):
    def __init__(self):
        super().__init__(title="Dashboard")
        self.set_decorated(False)
        self.fullscreen()

        css = b"""
        window {
            background-color: #000000;
        }
        button.tile {
            background: #111111;
            color: #ffffff;
            border-radius: 14px;
            border: 2px solid #2a2a2a;
            font: 18px monospace;
            padding: 18px;
        }
        button.tile:hover {
            background: #1a1a1a;
        }
        """

        provider = Gtk.CssProvider()
        provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        grid = Gtk.Grid()
        grid.set_row_spacing(30)
        grid.set_column_spacing(30)
        grid.set_halign(Gtk.Align.CENTER)
        grid.set_valign(Gtk.Align.CENTER)

        for i, (name, cmd) in enumerate(TILES):
            btn = Gtk.Button(label=name)
            btn.get_style_context().add_class("tile")
            btn.set_size_request(240, 140)

            if cmd:
                btn.connect("clicked", self.launch, cmd)
            else:
                btn.set_sensitive(False)

            grid.attach(btn, i % 3, i // 3, 1, 1)

        self.add(grid)
        self.show_all()

    def launch(self, _, cmd):
        subprocess.Popen(cmd)
        Gtk.main_quit()

if __name__ == "__main__":
    Dashboard()
    Gtk.main()
