# NCEMS Hub

Central landing page for North Country EMS operations tools. Clinical reference moved to its own site, clinical.northcountryems.org (repo `clinical`), in 2.0.

## Links

- Live (hub): [https://hub.northcountryems.org/](https://hub.northcountryems.org/)
- Clinical (separate since 2.0): [https://clinical.northcountryems.org/](https://clinical.northcountryems.org/)
- Repo: [https://github.com/emaildougb/apps](https://github.com/emaildougb/apps)
- Upload: [https://github.com/emaildougb/apps/upload/main](https://github.com/emaildougb/apps/upload/main)

## Files (upload ALL of these)

- `index.html`: crew-facing hub
- `apps.json`: the button list (edit this to add, remove or rename apps)
- `icons/` folder: the small app pictures on the buttons (shifts.png, fng.png, apparatus.png, ir.png, cgstaff.png). On GitHub, drag the whole icons folder in with the other files
- `logo.png`: NCEMS round logo (header)
- `apple-touch-icon.png`: home screen and tab icon
- `icon-512.png`: big icon for Android and the launch screen
- `manifest.json`: app mode settings
- `README.md`: this file

## Page layout

**One page (since 2.0), no sign-in:** Operations (Open Shifts, Incident Report) · Logistics (Apparatus Checker, Facilities & Grounds) · BC / Chief (CG Staff). Every button shows to everyone. Each app signs people in itself, and CG Staff turns away anyone not on its list
**Incident Report:** a red button next to Open Shifts in Operations. No sign-in, so volunteers can file
**Push Notice:** in the (i) info panel. Chiefs tap "BC / Chief: sign in to post a notice" there. That is the only sign-in on the hub. Notice banner pinned at the bottom
**Clinical reference:** not here anymore. It's its own site and repo: clinical.northcountryems.org (`clinical`)

## Home screen address

Tell everyone to save **https://hub.northcountryems.org/** to their home screen. Never hand out the github.io address. If the hub ever moves hosts, only the DNS record changes and nobody re-saves anything.

## Adding, removing or renaming an app (no index.html change)

1. Open `apps.json` in the repo and click the pencil
2. Copy an existing button line and change `title`, `sub` and `url`
   - `\n` in a title makes a line break (`"NCEMS\nOT"`)
   - `"style": "dark"` for the darker green card
   - `"soon": true` (and no url) for a grey Coming Soon card
   - Every button is listed under `"operations"`. `"style": "red"` makes a red button (Incident Report)
   - `"audience"`: `all` (default), `signedin`, `cgstaff` (command staff only), `admin` (push notice admins)
3. Commit. Every phone picks it up the next time the hub opens or comes back to the front. No re-adding the icon.

If `apps.json` has a typo or can't load, phones keep the last good list, or the buttons built into `index.html`.

## Updating index.html (rare)

1. Bump `HUB_VERSION` near the top of the script (`'1.12'` to `'1.13'`)
2. Upload. Open hubs show a blue "New version available. Tap to refresh" bar. One tap and they're current. No delete and re-add.

## Notices (since v1.14)

1. The notice banner is stored on Doug's Cloudflare Worker: `https://ncems-api.d-boyce.workers.dev/notice`. Anyone can read it; the hub checks every minute and whenever it's reopened
2. Push Notice is in the (i) info panel, shown to `ADMIN_EMAILS` after Microsoft sign-in. The Worker checks the sign-in itself (`NOTICE_ADMINS`, default Doug, Derek, Bryce), so nobody can post a notice by going around the hub
3. Firebase is no longer used (2.1). The usage counter is on the `ncems-checks` Worker

## Changelog

### v2.3
- Haptics: a light tick when you tap a button, link, tab or card, the same way the EP Checker does it. iPhone needs iOS 18 or newer with System Haptics on (Settings, Sounds & Haptics). Android phones vibrate. Nothing else changed

### v2.2
- Operations now holds Open Shifts and Incident Report
- The Apparatus & Reports section is now called Logistics and holds Apparatus Checker and Facilities & Grounds
- Changed apps.json, index.html (backup buttons and HUB_VERSION) and README.md

### v2.1
- Usage counter moved off Firebase to the `ncems-checks` Worker on Doug's NCEMS Cloudflare (281 old visits copied). The hub no longer loads Firebase at all

### v2.0
- New phone icon: NCEMS green and gold split corner to corner with four white tiles, NCEMS across the bottom (matches the Open Shifts icon). `apple-touch-icon.png` is the new icon and `icon-512.png` is the big one Android uses for the icon and the launch screen. Delete the old icon from the home screen and add it again to see it
- The hub is one page with no sign-in. Every button is right there when it opens: Open Shifts, Facilities & Grounds, Apparatus Checker, Incident Report, CG Staff. Each app signs people in itself. No tabs
- The Clinical tab moved to its own site, clinical.northcountryems.org (new repo `clinical`)
- Incident Report is a regular red button next to the Apparatus Checker (the Report tab is gone). No sign-in needed
- CG Staff button shows to everyone now and says "CG Staff only"; the CG Staff app itself only lets the command staff in (CG Staff 1.14 adds a CG Staff only box with a way back)
- Each button has the app's small icon above its name (files in the new `icons` folder: shifts, fng, apparatus, ir, cgstaff). apps.json sets them with `"icon"`
- The only sign-in left on the hub is in the (i) panel, for chiefs posting a notice. If you signed in there before, the hub still remembers you and passes your sign-in along to the other apps
- NCEMS OT button renamed Open Shifts and pointed at shifts.northcountryems.org (Derek renamed the app; the old overtime address forwards there)
- apps.json no longer has the clinical section or clinicalNotice

### v1.16
- CG Staff button now goes to https://cgstaff.northcountryems.org/ instead of the old github.io address (in apps.json and the built in fallback). Because it's a northcountryems.org address now, it also carries the sign in along, so CG Staff opens without typing

### v1.15
- Signing in from Operations now lands you back in Operations instead of the hub home
- Remembers who signed in. Next time it tries a quiet sign in, then goes through Microsoft without the account picker
- Links to other northcountryems.org apps (CG Staff, Facilities and Grounds, Overtime, EP Checker) carry `?login_hint=you@northcountryems.org` so those apps can sign you in without typing. CG Staff 1.9 and Facilities and Grounds 2.14 use it; Overtime needs Derek to add the same

### v1.14
- Security fix from the October 2026 audit: notices moved from Firestore (which anyone could write to) to the Cloudflare Worker, which only accepts posts from signed-in hub admins
- Notice text is cleaned before it shows in the popup, so a notice can't run code on crew phones
- iPhone: the bottom tab bar now runs to the bottom edge when there is no notice (no empty band under it)
- Hub version shows in the (i) panel; panel title now NCEMS Hub
- CG Staff button now also shows for k.reid@northcountryems.org
- Needs Worker 3.1 deployed first (adds `/notice`)

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
