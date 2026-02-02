##Install latest version of python
pkg install python3

##Install latest version of gtk3
pkg install gtk3

##Installing X11 base packages
pkg install xrog xinit xsetroot

##Installing i3 window manager
pkg install i3 i3status dmenu

##install required applications
pkg install firefox pcmanfm xterm

you can replace later:
pcmanfn -> thunar / nautilus
xterm -> alacritty / foot

##Create i3 config directory

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

# Omega_BSD - Initial UI (console-style)
# Window manager: i3
# Philosophy: Home button + fullscreen foreground app

font pango:monospace 11

# Black background
exec --no-startup-id xsetroot -solid "#000000"

# Visual spacing
gaps inner 20
gaps outer 60
smart_gaps on

# No window chrome
default_border pixel 0
default_floating_border pixel 0
focus_follows_mouse no

# All apps behave like console foreground apps
for_window [class=".*"] fullscreen enable
for_window [class=".*"] border pixel 0

# --- App launch / resume (scratchpad based) ---
# If app exists -> resume
# Else -> launch

bindsym F1 exec --no-startup-id sh -lc 'i3-msg "[class=Firefox] scratchpad show" || firefox'
bindsym F2 exec --no-startup-id sh -lc 'i3-msg "[class=Pcmanfm] scratchpad show" || pcmanfm'
bindsym F3 exec --no-startup-id sh -lc 'i3-msg "[class=XTerm] scratchpad show" || xterm'

# --- Home button ---
# Hide current app (do NOT kill) and show dashboard
bindsym Escape move scratchpad; exec --no-startup-id /root/dashboard.py

# Always start on workspace 1
exec --no-startup-id i3-msg 'workspace 1'

# Auto-start dashboard
exec --no-startup-id /root/dashboard.py

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


