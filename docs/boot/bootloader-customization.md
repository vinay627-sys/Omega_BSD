# OmegaBSD Bootloader Customization


## Scope
This document describes bootloader-level changes only. No kernel or userland behavior is modified.

Architecture tested:
- FreeBSD 15.0
- ARM64
- UTM (macOS host)

These changes are expected to be architecture-neutral.


## Boot Process Overview

1. EFI firmware
2. FreeBSD loader
3. Lua-based boot menu
4. Kernel handoff

Relevant directories:
- `/boot/loader.conf`
- `/boot/lua/`
- `/boot/logo-*.4th` (legacy)



## Implemented Changes

### Disable Default Logo

loader_logo="none"

Effect:
-> Prevents default ASCII orb/beastie rendering
-> Boot menu remains functional

## Using temporary own Logo
This is still in the beginning stage of understanding each and every file, 
Go to /boot/lua/gfx-orb.lua (This is default orb that gets rendered beside that boot menu) 
Lua uses mostly ascii rendering so use only that at least in the beginning of editing. 


### Boot Menu Text Customization

File modified:

/boot/lua/menu.lua

Change:
-> Replaced default welcome text with project branding

Outcome:
-> Confirms Lua-based loader UI is active
-> Overrides legacy `.4th` logic

## declutterring some messages after Bootmenu 
Go to /boot/loader.conf
add these lines:
boot_verbose="NO"
kern.msgbuf_showcons="0"

Go to /etc/rc.conf
add these lines:
rc_startmsgs="NO"
rc_debug="NO"
clear_tmp_enable="YES"
background_dhclient="YES"
dhclient_flags="-q"

## Restore / ensure console login works (important)
Check that ttyv0 is enabled and clean.

go to /etc/ttys
Check for the line "ttyv0   "/usr/libexec/getty Pc"    xterm   on  secure" if there are any changes change it to that line
save and exit
Apply the changes: sudo kill -HUP 1
verify: ps -ax | grep '[g]etty.*ttyv0'

## Make MOTD persistent
after we login into the terminal we get a greetings message like "welcome to FreeBSD etc etc". i have changed it to my brand name and the deleted that text
there are 2 files /etc/motd and /etc/motd.template. change what ever you want in motd.template not in motd. 
Go to /etc/motd.template and edit your changes like add a ascii logo and your own welcome template
FreeBSD will regenerate /etc/motd from this on every boot.

If there is any sort of future update in FreeBSD there is a chance that your welcome templete maybe be reverted back to original format or straight up doesnt render at all
So go to rc.conf
ADD this line -> update_motd="NO"

After login lets say you wanted to start from beginning of the page rather than at the end with only seeing your welcome page for only a second
go to ~/.profile (This is your shell profile)
Add these lines
clear
cat /etc/motd.template
sleep 1
clear

##important while doing these changes 
Please enable SSH right from the start if there are any weird rendering issues or terminal problems you can just use ssh to rectify those mistakes easily and always keep a stock back up file if things go wrong (which it will).
## Findings

-> `.4th` logos are ignored when Lua menu system is active
-> `loader_logo=<custom>` silently falls back if no Lua handler exists
-> Lua drawer is the authoritative render path in modern FreeBSD
-> Basically after FreeBSD 13 they have chosen lua as their boot loader menu as a deterministic function.


## Stability Notes

-> Bootloader survived multiple Lua errors
-> System always recoverable via loader prompt (`boot`)
-> No kernel panic encountered

Important notes:
	•	❌ .4th files are legacy
	•	✅ Lua (/boot/lua/*.lua) is authoritative
	•	menu.lua controls menu structure
	•	drawer.lua controls rendering
	•	loader.conf only toggles flags, not logic


## Portability Notes

These changes:
- Do not touch kernel
- Do not rely on CPU architecture
- Should port 1:1 to x86_64
