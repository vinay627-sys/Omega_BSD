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
File called config code


Go to file directory (/root/dashboard.py)

Paste the following code
File called dashboard.py in the repository. 

## Permissions(important)

Make the dashboard executable

-> chmod +x dashboard.py

##i/scripts/home.sh

Optional “Home” helper (if you prefer script-based control).

Example home.sh (console-style: hide app → show dashboard):

#!/bin/sh
i3-msg move scratchpad >/dev/null 2>&1
exec /root/dashboard.py


