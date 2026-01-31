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


### Boot Menu Text Customization

File modified:

/boot/lua/menu.lua

Change:
-> Replaced default welcome text with project branding

Outcome:
-> Confirms Lua-based loader UI is active
-> Overrides legacy `.4th` logic


## Findings

-> `.4th` logos are ignored when Lua menu system is active
-> `loader_logo=<custom>` silently falls back if no Lua handler exists
-> Lua drawer is the authoritative render path in modern FreeBSD
-> Basically after FreeBSD 13 they have chosen lua as their boot loader menu as a deterministic function.


## Stability Notes

-> Bootloader survived multiple Lua errors
-> System always recoverable via loader prompt (`boot`)
-> No kernel panic encountered



## Portability Notes

These changes:
- Do not touch kernel
- Do not rely on CPU architecture
- Should port 1:1 to x86_64
