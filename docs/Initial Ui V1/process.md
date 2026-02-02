## Install latest version of python
pkg install python3

## Install latest version of gtk3
pkg install gtk3

## Installing X11 base packages
pkg install xrog xinit xsetroot

## Installing i3 window manager
pkg install i3 i3status dmenu

## install required applications
pkg install firefox pcmanfm xterm

you can replace later:
pcmanfn -> thunar / nautilus
xterm -> alacritty / foot

## Create i3 config directory

mkdir -p ~/.config/i3

## Start i3 under VNC
When using TigerVNC, i3 is usually started via ~/.xinitrc

1) nano ~/.xinitrc
2) type: exec i3 (save and exit)
3) chmod +x ~/.xinitrc

Then start VNC:
vncserver :1
connect from host: localhost:5901

(Start the process of VNC after the below commands)


Go to file directory ("~/.config/i3/config)

Paste the following code



Go to file directory (/root/dashboard.py)

Paste the following code

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

##Permissions(important)

Make the dashboard executable

chmod +x dashboard.py

##i/scripts/home.sh

Optional “Home” helper (if you prefer script-based control).

Example home.sh (console-style: hide app → show dashboard):

#!/bin/sh
i3-msg move scratchpad >/dev/null 2>&1
exec /root/dashboard.py


