# NCEMS Hub

Central landing page for North Country EMS crew and admin tools.

## Links

- Live (hub): [https://emaildougb.github.io/apps/](https://emaildougb.github.io/apps/)
- Repo: [https://github.com/emaildougb/apps](https://github.com/emaildougb/apps)
- Upload: [https://github.com/emaildougb/apps/upload/main](https://github.com/emaildougb/apps/upload/main)

## Files (upload ALL of these)

- `index.html` — crew-facing hub
- `apps.json` — the button list (edit this to add, remove or rename apps)
- `logo.png` — NCEMS round logo (header)
- `apple-touch-icon.png` — iOS home-screen + tab icon
- `manifest.json` — standalone app-mode config
- `README.md` — this file

## Page layout

**Page 1 (swipe):** Clinical reference (big SF Mono, one per row) + Quick Protocols
**Operations tab (Microsoft sign-in):** Operations (NCEMS OT, Facilities & Grounds) · Apparatus (Apparatus Checker) · BC / Chief (CG Staff, command staff accounts only)
**Report tab:** Incident Report
**Push Notice:** in the (i) info panel, admin accounts only
Tap the dots under the header or swipe to switch. Notice banner pinned at bottom on both.

## Home screen address

Tell everyone to save **https://hub.northcountryems.org/** to their home screen. Never hand out the github.io address. If the hub ever moves hosts, only the DNS record changes and nobody re-saves anything.

## Adding, removing or renaming an app (no index.html change)

1. Open `apps.json` in the repo and click the pencil
2. Copy an existing button line and change `title`, `sub` and `url`
   - `\n` in a title makes a line break (`"NCEMS\nOT"`)
   - `"style": "dark"` for the darker green card
   - `"soon": true` (and no url) for a grey Coming Soon card
   - `"clinicalNotice"` at the top of the file is the Clinical tab warning. Change the words or set it to `""` to remove it
   - `"audience"`: `all` (default), `signedin`, `cgstaff` (command staff only), `admin` (push notice admins)
3. Commit. Every phone picks it up the next time the hub opens or comes back to the front. No re-adding the icon.

If `apps.json` has a typo or can't load, phones keep the last good list, or the buttons built into `index.html`.

## Updating index.html (rare)

1. Bump `HUB_VERSION` near the top of the script (`'1.12'` to `'1.13'`)
2. Upload. Open hubs show a blue "New version available. Tap to refresh" bar. One tap and they're current. No delete and re-add.

## Clinical card order (Page 1)

Intubation (live) · Advanced Airway · Drip Sets · Medication List · Shock · Sepsis · Stroke · Cardiac (all coming soon) · Quick Protocols (live)

## Firebase setup (notices)

1. Firebase config lives in `index.html`
2. Push Notice is in the (i) info panel, shown only to `ADMIN_EMAILS` after Microsoft sign-in

## Changelog

### v1.13
- Removed `admin.html` (old password page with the password in plain text). Push Notice stays in the (i) panel behind Microsoft sign-in for Doug, Derek and Bryce
- Header now reads NCEMS Hub (was NCEMS Field Reference); tab title NCEMS Hub
- Home button (house icon) in the header; tapping the logo or title also goes home (Clinical tab, scrolled to top)
- Clinical tab warning above Intubation: "For clinical reference only. Not to be used for patient care." Text lives in `apps.json` as `clinicalNotice`; set it to "" to hide it once approved
- Playwright smoke test: header, home button, warning from apps.json, hide when empty

### v1.12
- Buttons now come from `apps.json`, so adding or changing an app is a one file edit, no hub code change
- Last good `apps.json` is kept on the phone for no signal; built-in buttons stay as a final fallback
- Self update: the hub checks the live `HUB_VERSION` when it opens and when it comes back to the front, and shows a one tap refresh bar if there's a newer version
- Playwright smoke test: 10/10 (CG Staff shows only for command staff, apps.json edits show up, offline fallback, update bar)

### v1.11
- Operations tab: new BC / Chief section with a CG Staff button (https://emaildougb.github.io/cg-staff/) under Apparatus
- Only shows for command staff accounts in `CG_STAFF_EMAILS` (Doug, Derek, Dennis, Bryce, Chuck, Nick). Everyone else never sees it
- The CG Staff app checks the login again on its own, so the button is not the lock
- Playwright smoke test: button hidden for crew, shown for CG Staff, links correctly

### v1.10
- Operations tab: new Facilities section with a Grounds Tracker button (https://emaildougb.github.io/grounds-tracker/), between Apparatus and BC / Chief
- Grounds Tracker has its own Microsoft sign-in, so the link is protected even outside the 5142 gate
- Playwright smoke test: unlock with 5142, Grounds Tracker button shows and links correctly

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
- iOS home-screen caching is handled by the update bar (v1.12). Only delete and re-add the icon if the bar never shows
- Each individual app still needs its own back button to `https://emaildougb.github.io/apps/`
