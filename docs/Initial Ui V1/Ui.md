# Console-Style FreeBSD Desktop

A minimalist, console-inspired desktop environment built on **FreeBSD**, designed around a **Home-button UX**, fullscreen foreground apps, and a launcher-style dashboard.

This project intentionally avoids traditional desktop paradigms (panels, docks, multitasking chaos) and instead follows a **PS-style appliance philosophy**.

---

## Goals

- Single-user, personal system
- Clean black home screen
- Launcher-based UI (apps open on demand)
- One foreground app at a time
- Home button behavior (hide app, return to dashboard)
- No DRM / Wayland dependency
- VM-friendly during development
- Portable to bare metal later

---

## Architecture
FreeBSD
│
├─ X11 (via TigerVNC / Xvnc)
│
├─ i3 Window Manager
│   ├─ Fullscreen-only apps
│   ├─ Scratchpad for background apps
│   └─ F-key navigation (VNC/macOS safe)
│
└─ Custom GTK Dashboard (Python)
├─ Black fullscreen launcher
├─ 6 centered tiles
└─ Click to launch apps

---

## Interaction Model

| Key | Action |
|----|-------|
| **F1** | Firefox (resume if running, else launch) |
| **F2** | File Manager |
| **F3** | Terminal |
| **Esc** | Home button (send app to background + show dashboard) |
| Mouse | Select launcher tile |

Apps are **not killed** on Home — they are backgrounded using i3’s scratchpad.

---

## Current Stack

- **OS**: FreeBSD (aarch64)
- **Display**: X11 (TigerVNC)
- **WM**: i3
- **Dashboard**: GTK3 (Python)
- **Host during dev**: macOS (VNC)
- **Target**: Bare metal desktop

---

---

## Known Issues

- Firefox tabs may close when scratchpad behavior changes  
  (acceptable for current prototype)
- No animations or sound yet
- Dashboard visuals are functional, not final

---

## Roadmap

### Short Term
- Stabilize background app behavior
- Improve dashboard visuals
- Add startup chime
- Add boot → dashboard transition

### Long Term
- Bare-metal deployment
- Fixed hardware profile
- Replace GTK dashboard with lighter UI
- Console-grade polish

---

## Philosophy

This is **not a desktop OS**.

It is a **personal console system**:
- deterministic
- distraction-free
- intentional

Everything visible.  Nothing accidental.

Final UI outcome <img width="1135" height="931" alt="Final UI" src="https://github.com/user-attachments/assets/582c9056-33cb-4431-9544-0c0d17762119" />


