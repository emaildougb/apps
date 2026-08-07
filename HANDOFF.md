# HANDOFF — apps (NCEMS Field Reference Hub)

## What it does

The central landing page that links out to all the other NCEMS crew/admin tools (Intubation, WAMBOchecker, onduty-incident-report, plus several "coming soon" cards like Advanced Airway, Drip Sets, Medication List, Shock, Sepsis, Stroke, Cardiac). Currently v1.8.

Layout is a bottom tab bar: **Clinical** (default — the live/coming-soon reference cards + Quick Protocols) and **Operations** (Incident Report, NCEMS OT, WAMBOchecker), gated behind a 4-digit access code (`5142`, hardcoded in page source) that unlocks once and stays unlocked until the app fully closes, then re-locks. A notice banner is pinned at the bottom of both tabs, backed by Firebase Firestore for live push updates from admin.

`admin.html` is a separate page (BC/Chief login) for pushing that notice banner — password-gated (`ADMIN_PASSWORD`, hardcoded, defaults to `"ncems2026"`), writes to the same Firestore doc.

## Where the data lives

- **Notices: Firebase Firestore**, document `notices/active`. `index.html` subscribes with `onSnapshot` for live updates; `admin.html` writes to that same document. This is the only piece of this whole app set that uses a real live backend rather than localStorage/manual sync.
- **Firebase config is a placeholder** in both `index.html` and `admin.html` (`authDomain: "PASTE.firebaseapp.com"`, etc.) — until someone pastes real Firebase project credentials into both files and flips `FIREBASE_READY = true`, notices don't work and the UI shows a "Firebase not connected yet" warning.
- **No localStorage use found** in `index.html` — the ops access-code unlock appears to be in-memory only (per the README: "unlocks once, stays unlocked until the app fully closes"), so it resets on every app relaunch, not persisted to disk.
- `manifest.json` — standard PWA manifest (name, icons, standalone display, theme color `#1C3A1C`), no data, just home-screen/app-mode config.

## Structure

- `index.html` — crew-facing hub (both tabs, notice display, Firestore listener).
- `admin.html` — BC/Chief login + notice-push form, separate Firestore write path.
- `logo.png`, `apple-touch-icon.png` — branding/icons.
- `manifest.json` — PWA config.
- `README.md` — detailed and current: links, file list, page layout, Firebase setup steps, full v1.0–v1.8 changelog including jsdom smoke-test pass counts per version.

## Anything odd

- **Firebase config is unfinished (`"PASTE.firebaseapp.com"`) in both files as shipped.** If this is deployed as-is, the notice banner silently does nothing but show "not connected" — worth checking whether a real config was ever pasted in before assuming notices work in production.
- **`ADMIN_PASSWORD = "ncems2026"` is hardcoded in `admin.html`** with a `// CHANGE THIS before deploying` comment right next to it — same "adequate for a small department, not real security" pattern as WAMBOchecker and onduty-incident-report. Worth confirming this was actually changed.
- **Ops access code `5142` lives in page source** — the README calls it out itself as "a placeholder gate only," with a note that real protection (Firebase Auth) is planned but not done.
- **iOS Safari sheet limitation, explicitly documented as unfixable by this app**: tapping into another app (Intubation, WAMBOchecker, etc.) from the hub opens it in a Safari sheet, not full-screen, because that's how iOS handles links from a home-screen web app. Each sub-app only runs full-screen if added to the home screen on its own — this is an iOS platform rule, not a bug in this codebase.
- Hosted in the `apps` repo specifically so it never collides with the root GitHub Pages URL — worth knowing if you're ever restructuring the org's repos.
- Same iOS home-screen cache-busting requirement as the other apps: delete and re-add the icon after every deploy.
