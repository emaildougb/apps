# NCEMS Field Reference Hub

Central landing page for North Country EMS crew and admin tools.

## Links

- Live (hub): [https://ncemsderek.github.io/apps/](https://ncemsderek.github.io/apps/)
- Live (admin): [https://ncemsderek.github.io/apps/admin.html](https://ncemsderek.github.io/apps/admin.html)
- Repo: [https://github.com/ncemsderek/apps](https://github.com/ncemsderek/apps)
- Upload: [https://github.com/ncemsderek/apps/upload/main](https://github.com/ncemsderek/apps/upload/main)

## Files (upload ALL of these)

- `index.html` — crew-facing hub
- `admin.html` — BC/Chief login to push notices
- `logo.png` — NCEMS round logo (header)
- `apple-touch-icon.png` — iOS home-screen + tab icon
- `manifest.json` — standalone app-mode config
- `README.md` — this file

## Page layout

**Page 1 (swipe):** Clinical reference (big SF Mono, one per row) + Quick Protocols
**Page 2 (swipe):** Operations + Apparatus (WAMBOchecker)
Tap the dots under the header or swipe to switch. Notice banner pinned at bottom on both.

## Clinical card order (Page 1)

Intubation (live) · Advanced Airway · Drip Sets · Medication List · Shock · Sepsis · Stroke · Cardiac (all coming soon) · Quick Protocols (live)

## Firebase setup (notices)

1. Paste your Firebase config into both `index.html` and `admin.html`
2. Set `FIREBASE_READY = true` in both files
3. Change `ADMIN_PASSWORD` in `admin.html` before deploying

## Changelog

### v1.8
- Added a line to the info panel: apps open in a Safari window; for full-screen, add them to the home screen individually
- jsdom smoke test: 5/5 pass

### v1.7
- Notice banner: smaller (38px), white centered text, tap it to expand the full notice in a popup
- Info panel now reads "contact Doug" and the email opens with subject line "NCEMS HUB APP"
- Ops access code (5142) resets every 2 hours, and re-locks when the app returns to foreground past that window
- Added manifest.json for clean standalone app-mode launch from the home screen
- NOTE on app mode: links to other apps open in an iOS Safari sheet, not full-screen — that's an iOS rule the hub can't override. Each app runs full-screen only when added to the home screen on its own.
- jsdom smoke test: 15/15 pass

### v1.6
- Removed swipe. Bottom tab bar now: Clinical (default) | Operations
- Operations tab locked with code 5142 — unlocks once, stays unlocked until the app fully closes
- Operations holds Incident Report, NCEMS OT, WAMBOchecker
- (i) info button top-right of header — credits Doug with a one-line note and a tap-to-email link (d.boyce@northcountryems.org)
- NOTE: 5142 lives in page source — placeholder gate only. Move to Firebase Auth for real protection (planned)
- jsdom smoke test: 20/20 pass

### v1.5
- Clinical + Quick Protocols cards now use the Intubation Guide's button style: tall forest-green gradient cards, big bold uppercase SF Mono titles, press-to-scale, no confirm on tap
- Ops/Apparatus buttons (Incident Report, NCEMS OT, WAMBOchecker) match the same family
- Coming Soon cards use a muted version of the same button shape
- SF Mono set as the hub's base font to match the clinical apps
- jsdom smoke test: 12/12 pass

### v1.4
- NCEMS round logo in header, iOS home-screen icon, and favicon
- Removed all emoji icons (the source of the garbling) — clean text + logo only
- Resized logo to web-friendly PNG (was a 2.5 MB / 3375px JPEG)
- Hardened swipe script for older iOS Safari
- jsdom smoke test: 12/12 pass

### v1.3
- Two swipe pages; clinical big-word cards; Quick Protocols separate section

### v1.2
- Full hub rebuild; admin notice banner; admin.html with login

### v1.1
- Config-driven APPS list; added NCEMS OT

### v1.0
- First build

## Notes

- Hosted in `apps` repo — never touches root URL
- iOS home-screen caches hard — delete and re-add icon after every deploy
- Each individual app still needs its own back button to `https://ncemsderek.github.io/apps/`
