# NCEMS Hub

Version 3.14. Three views at one address: **Wall** (the station TV, cycles on its own), **Desk** (station and office computers) and **Pocket** (phones and iPads). Everyone signs in with their NCEMS Microsoft account because the Hub shows crew information. Clinical reference lives at clinical.northcountryems.org (repo `clinical`).

## Links

- Live (hub): [https://hub.northcountryems.org/](https://hub.northcountryems.org/)
- Clinical (separate since 2.0): [https://clinical.northcountryems.org/](https://clinical.northcountryems.org/)
- Repo: [https://github.com/emaildougb/apps](https://github.com/emaildougb/apps)
- Upload: [https://github.com/emaildougb/apps/upload/main](https://github.com/emaildougb/apps/upload/main)
- Training calendar, printable page (no sign in): [https://hub.northcountryems.org/training.html](https://hub.northcountryems.org/training.html)
- Training calendar data (built by the Training Dept project, don't edit by hand): [https://raw.githubusercontent.com/emaildougb/apps/main/training-events.json](https://raw.githubusercontent.com/emaildougb/apps/main/training-events.json)

## Files (upload ALL of these)

- `index.html`: crew-facing hub
- `apps.json`: the button list (edit this to add, remove or rename apps)
- `training-events.json`: the training calendar dates. Built from the Excel master by the Training Dept project, never edited by hand (see How to add a training date)
- `training.html`: the printable training calendar page, no sign in (reads training-events.json)
- `tools/excel_to_training_json.py`: turns the Event List tab of NCEMS_Training_Calendar.xlsx into training-events.json (for the Training Dept project, not used by the pages)
- `icons/` folder: the small app pictures on the buttons (shifts.png, fng.png, apparatus.png, ir.png, cgstaff.png). On GitHub, drag the whole icons folder in with the other files
- `logo.png`: NCEMS round logo (header)
- `apple-touch-icon.png`: home screen and tab icon
- `icon-512.png`: big icon for Android and the launch screen
- `manifest.json`: app mode settings
- `README.md`: this file

## Page layout (3.2)

- **Sign in first.** Microsoft sign in (NCEMS Hub app registration 54eb93f5), NCEMS accounts only
- **Desk** (computers, 3.2): left sidebar (Today, Schedule, Daily tasks, Training and events, Training videos, Vehicle checks, Weather, Station notes, LMS, Fire District 13; the Soon ones say what's coming), a search box (names on today's and tomorrow's crews, rigs, tasks, apps, pages) and the station picker on top. **Today** shows Crews today (one card per unit, Station 51 on the left, Station 52 on the right, shop number in the corner, open seats in orange), Duty battalion chief (Soon) with the weather, three numbers (vehicles checked today live; crew coverage and training completion show once Open Shifts and the LMS are connected), today's duties with check offs and the BC add box, and Station notes (the posted notice). **All the apps sit in one line along the bottom**
- **Pocket** (phones and iPads, picked automatically): the same panels one at a time with a bottom tab bar (Today, Checks, Duties, Weather, Apps)
- **Wall**: pick **Rotate every** on Desk (5, 10 or 15 seconds, or Custom from 3 to 20; remembered on that computer, default 10), then tap **Wall**. The screen goes full screen and cycles through Today (who's on each unit), Vehicle checks, Duties and Weather (a slide with no data is skipped). **Keys:** left and right arrows change slides, Space pauses, Enter continues. It stays the Wall on that computer after a restart. Esc goes back to Desk. Moving the mouse shows the key help for a few seconds. `?wall=1` turns it on, `?wall=0` off
- **Station** picker in the top bar (51 or 52) sets the weather point and is remembered per device
- **Notice:** chiefs post it from the (i) panel (d.boyce, d.langdon, d.madler, b.shirley see it; the ncems-api Worker is the real gate). Shows on every view and every Wall slide
- **Incident Report** stays a regular app button. Volunteers who don't sign in to the Hub go straight to reports.northcountryems.org

## Training calendar (since 3.11)

- **On the Hub:** Desk sidebar **Training calendar**, phone tab **Training**. Month grid that opens on this month, arrows for other months, Today button, chips to show or hide each type, tap a day for the full title, time and notes, Upcoming (next 10) and a legend. Phones get a list instead of a grid. **Print** prints just the month, landscape, no buttons
- **Printable page, no sign in:** https://hub.northcountryems.org/training.html, same data, NCEMS navy and blue, for the training office and for sharing. `?month=2026-12` opens December 2026, `?print=1` opens the print dialog. Example: https://hub.northcountryems.org/training.html?month=2026-12&print=1
- **Data:** both pages read `training-events.json`. Nobody edits index.html or training.html to change dates
- **Privacy:** training-events.json and training.html can be opened by anyone with the link (like apps.json). Keep notes to scheduling info: who is on duty for a class is fine, nothing personal or medical

## How to add a training date

There is one way to change the calendar, so the Excel master and the live calendar never disagree. The master is OneDrive > Claude > Training > NCEMS_Training_Calendar.xlsx, tab **Event List**. Don't edit training-events.json on GitHub by hand: the next rebuild from the Excel would wipe the change out.

1. In the **Training Dept** Claude project, say what changed in plain words, for example "Add OTEP airway skills on January 14, 0900 to 1100" or "Move the December 29 ACLS to January 5".
2. The project first compares the live training-events.json with the Excel and asks about anything that doesn't match.
3. It updates the Event List in the Excel, then builds a new training-events.json with `tools/excel_to_training_json.py`.
4. Open https://github.com/emaildougb/apps/upload/main
5. Drag in training-events.json (same name, it replaces the old one).
6. Click **Commit changes**.
7. Tell the project "uploaded". It checks the raw file for the change and merge conflict markers, and checks https://hub.northcountryems.org/training.html. The Hub, Wall and printable page update within about a minute (an open screen within 30 minutes, or right away on refresh).

**What the file looks like** (for reference, the Training Dept project writes it):

One day:

```json
{"title":"OTEP: Airway skills","type":"otep","date":"2027-01-14","time":"0900–1100","notes":"Station 51 training room"}
```

A range of days (`days` and `exclude` are optional; leave out `days` for every day in the range). The pages read ranges, but the converter writes one day per Excel row:

```json
{"title":"PEAC Static Station","type":"peac","start":"2026-11-30","end":"2026-12-31","days":["Mon","Tue","Wed","Thu"],"exclude":["2026-12-21","2026-12-22"],"time":"On shift","notes":"Remediation also runs here"}
```

**Fields:** `title` (required), `type`, `date` for one day, or `start` and `end` for a range, `days` (Sun Mon Tue Wed Thu Fri Sat), `exclude` (dates to skip), `time` and `notes` (optional, shown when someone taps the day).

**Types:** acls, pals, peac, advcardiac, otep, pcep, ftep, off, holiday. **A new type** is one line under `"types"` in training-events.json and one line in the TYPES list at the top of `tools/excel_to_training_json.py` (ask the NCEMS APPS project). No page change.

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

### v3.14 (11/16/2026)
- **Wall Daily Snapshot shows plain words, not copied text.** Each briefing item shows a cleaned title (source tags like "(10/15-10/17 shift notes)" and RE:/FW: removed) and under it the short line a BC wrote in CG Staff (**Line for the Hub Wall**, CG Staff 1.34). With no line, it shows who has it and the group. The raw card details never show on the Wall. The Desk card shows the line too, or the details when there is no line
- Neuro interventional coverage is **PeaceHealth Southwest (PHSW)**, not Legacy Salmon Creek. November 2026 schedule loaded (no coverage Nov 14, 15, 26, 28 and 29)
- Needs ncems-checks Worker 1.11 (passes the `say` line through)

### v3.13 (11/16/2026)
- **Daily Snapshot.** First slide on the Wall, a card at the top of Desk Today, the top of the phone's Today tab, and the Desk page that used to be Station notes (renamed Daily Snapshot; the posted notice now shows under it as "Posted notice")
- Top line: whether **neuro interventional at PeaceHealth Southwest (PHSW)** is covered today (green covered, red not covered, gray no schedule), with hours or a note when the schedule has one
- Below it: the Shift Ops cards flagged **Mention at shift briefing** in CG Staff (Briefing = Yes, not Completed), with the triage color, details and owner
- How it gets here: a scheduled Claude task reads the PHSW monthly neuro intervention Excel (from the PeaceHealth Transfer Center, forwarded by Chief Shirley) from Doug's email and writes `nir-coverage.json` in the CG Staff SharePoint folder "Neuro IR Coverage (do not delete)". When Doug, Derek, Dennis or Bryce has CG Staff open (1.33 or newer), CG Staff sends the flagged cards and that file to the ncems-checks Worker (1.10, POST /fleet/brief/sync). The Hub reads GET /fleet/brief. Crews never need access to the CG Staff site
- If the list is more than 36 hours old the Hub says so (it refreshes when a BC or the Chief opens CG Staff)

### v3.12.2 (11/16/2026)
- Wall: This week in training shows every rotation now. When nothing is on the calendar this week it says so and lists what's coming up next (up to 5)

### v3.12.1 (11/16/2026)
- Training calendar has one update path now: the Training Dept project updates the Excel master first, then builds training-events.json. The hand edit on GitHub steps are gone from this README so the Excel and the live calendar can't drift apart. The project also compares the live file with the Excel before each build

### v3.12 (11/16/2026)
- **Wall: This week in training.** New slide after Open shifts with today plus the next 6 days from training-events.json (day, type tag, title, time). It is skipped when nothing is on the calendar that week. Up to 8 lines (7 when a notice is up), then "And N more this week on the Hub"

### v3.11 (11/16/2026)
- **Training calendar.** New Desk page (sidebar, replaces Training and events Soon) and phone tab. Month grid, filter chips, tap a day for details, Upcoming, legend, Print (landscape, one month, no buttons). Phones get a list view under 600 px wide
- **Printable page** `training.html` with no sign in, in NCEMS navy and blue, for the training office and sharing. `?month=YYYY-MM` and `?print=1`
- **Data file** `training-events.json`: dates and types live here, so changing training never touches code. Supports one day (`date`) and ranges (`start`, `end`, `days`, `exclude`). New types are one line under `types`

### v3.10 (11/15/2026)
- **Rigs on the crew cards match what each unit is really in.** Medic crews always check their primary ambulance first, so the first rig checked today by someone on a unit's crew is that unit's rig (Desk Today, Schedule, Wall). If nobody on the crew has checked yet, it uses a rig claimed for that unit in the Checker, then the unit's usual rig (marked last known). One rig per unit
- Vehicles checked today and the Vehicle checks list use the same matching, so a rig nobody is in today doesn't count against the percent

### v3.9 (11/15/2026)
- **Duty battalion chief is live** from Derek's board feed (https://ncems-ot.d-langdon.workers.dev/hub/board, Hub ID token). Rule from Doug: if Derek Langdon or Dennis Madler is on the schedule anywhere that duty day (BC row or any medic unit), they are the duty BC. If one of them is on and Doug is too, Doug shows underneath as Training chief. If neither is on, Doug is the duty BC. Duty day rolls over at 07:30. Shows on Desk Today and in the Wall Today subtitle
- **Apps sit at the end of Today** instead of floating over the page, so nothing scrolls under them. New **Apps** page in the sidebar under Training Status
- Top bar: search box is shorter and says Search, so Rotate Custom and Wall stay on one line
- Vehicles checked today counts only rigs a crew is on today. Out of service rigs and spares don't count
- Crew cards no longer say "Open, 1 of 2 staffed" (Desk, Schedule and Wall)
- Daily tasks: says "Crew can log in to check complete". No more name and time on who checked a task off (Desk, phone, Wall, search)
- Weather: the next 24 hours is a line graph (temperature line, chance of rain shaded, dashed line at freezing) on Desk, phone and Wall instead of the boxes
- District map: air quality and earthquakes removed (Derek: too crowded). Added a QR code for the live helicopter map on phones (globe.adsb.lol, free, no app, same feed the map uses), with an Open it here link on Desk

### v3.8 (11/15/2026)
- **Duties per station.** Station 51 and Station 52 each have their own weekly duty list. Station 51 keeps the current checklist and its old check offs. Station 52 starts empty (it says so) until Doug sends its list; chiefs can still add tasks for the day there
- Tasks a chief adds are saved to the station on screen (needs ncems-checks 1.9, ids a:51:... and a:52:...). Older added tasks with no station show on Station 51
- **Station accounts lock the Hub.** Signed in as station51@ the Hub stays on Station 51; station52@ stays on Station 52. The station picker turns into a plain label. Personal accounts keep the picker
- To change a station's weekly list later, edit WEEK51 or WEEK52 near the top of index.html (one line per day)

### v3.7 (11/15/2026)
- **Open shifts are live.** Derek made read only Hub feeds (no names): https://ncems-ot.d-langdon.workers.dev/hub/open-shifts (Crew 1, medic) and https://ncems-c2.d-langdon.workers.dev/hub/open-shifts (Crew 2, EMT), Microsoft ID token, hub.northcountryems.org allowed. The Hub shows the next 7 days
- Desk: Open shifts page lists each open shift (day, unit, crew, hours) with a Sign up in Open Shifts button. Today's middle number is now Open shifts, next 7 days with Crew 1 and Crew 2 counts
- Wall: Open shifts slide right after Today (only when something is open). Phone: the list is on the Today tab
- Refreshes every 5 minutes

### v3.6.3 (11/15/2026)
- Apps in two rows of three on Desk and phones: HOSCAP, Open Shifts, Apparatus Checker on top; Facilities & Grounds, Incident Report, CG Staff underneath. Desk tiles have the logo on the left. During Duty Incident Report shows as Incident Report. HOSCAP button opens HOSCAP (each person signs in with their own login)

### v3.6.2 (11/15/2026)
- District map background switched to Esri's dark gray map (no key). CARTO's free map started showing "API key required". Radar a little lighter so roads show through

### v3.6.1 (11/15/2026)
- Road cameras load right away (they waited for a scroll on some screens). Earthquakes now counted within 40 miles of the district

### v3.6 (11/15/2026)
- **District map** (idea from God's Eye View, godseyeview.ai, kept to our district). Desk sidebar page, phone Weather tab, and two new Wall slides (District map, Roads)
- Layers, all free public feeds: dark map (Esri dark gray canvas, OpenStreetMap data), NOAA weather radar, wildfires and perimeters (NIFC WFIGS, prescribed burns counted separately), earthquakes near Mount St. Helens and the district for 7 days (USGS), air quality at Stations 51 and 52 (Open-Meteo), helicopters in the air within about 60 miles (public ADS-B through ncems-checks 1.8 /fleet/air), four WSDOT road cameras (SR 503 Rock Creek Rd, SR 503 Main St Battle Ground, SR 503 179th St, I-5 Woodland)
- Refresh: helicopters 30 seconds, fires, quakes and air 10 minutes, cameras 2 minutes, radar 5 minutes
- Leaflet 1.9.4 from cdnjs draws the map

### v3.5 (11/15/2026)
- App logos are back. Apps are tiles with the logo on top and the name under it (no descriptions), the same on Desk (one row along the bottom, longer names get a wider tile) and on phones (three across, one grid, no section labels)
- iPhone matches Desk: Today shows the Crews today cards, duty BC and weather, the three numbers and Station notes. Checks, Duties, Weather and Apps tabs use the same panels. Clock hidden, no sideways scrolling

### v3.4 (11/14/2026)
- Desk sidebar: Open shifts page after Schedule. Shows a button to the Open Shifts app until Derek adds the Hub to his feed, then it will list the open shifts

### v3.3 (11/14/2026)
- Rotate and Wall moved to the top bar next to the station picker. Station picker lists FD13 (coming soon)
- Apps along the bottom: bigger, title only (up to two lines, full words), no red line
- Duties added by a chief show the title: BC Boyce, BC Langdon, BC Madler, Chief Shirley, AC Robertson, AC Schutts. Only those six can add or remove tasks (ncems-checks 1.7)
- Wall: no Back to Desk button. Esc goes back to Desk (leaving full screen does too)
- Sidebar: LMS is now Training Status (Soon). Fire District 13 moved to the station picker

### v3.2 (11/14/2026)
- Desk redone to Doug's picture: sidebar pages, search, Crews today cards, Duty BC and weather, three number strip, duties and Station notes side by side
- Apps moved to one line across the bottom of the screen on Desk (Pocket keeps its Apps tab)
- Wall speed picker on Desk: 5, 10, 15 seconds or Custom (3 to 20). Was a fixed 20 seconds
- Wall keys: arrows for next and previous slide, Space to pause, Enter to continue. A Paused label shows at the bottom while paused
- On Desk's Today page the notice shows in Station notes instead of the banner (urgent notices still show the banner). Pocket and the Wall are unchanged

### v3.1
- **On shift today** on Desk and Pocket and a **Today** slide first on the Wall: Station 51 on the left, Station 52 on the right, each unit under the station of the rig its crew claimed (no claim yet: its primary rig, marked last known). Call sign big, First out / Third out / Summer unit with the rig (25A, not M25A), Crew 1, Crew 2, Crew 3, amber "1 of 2 staffed" when short. Tomorrow's crews listed under it on Desk
- Data from the ncems-checks Worker 1.6 /fleet/hub in one call: crews (fleet_crews, copied from Derek's schedule every hour at :17), today's vehicle checks and today's duty check offs
- Duties: check items off on Desk or Pocket (who and when shows on the Wall). BCs and Checker admins (ncems-checks ADMINS and READERS) can add a task for today and remove added ones
- Vehicle checks now live. Rig numbers show without the M (25A, 19)
- Still to come: open shifts (Derek adding the Hub to ncems-ot and ncems-c2) and the duty BC (not in the schedule feed)

### v3.0
- New dark Hub with three views: Wall (station TV slideshow), Desk (computers) and Pocket (phones and iPads, bottom tabs). Built from the Wall, Desk and Pocket mockup
- Microsoft sign in required to see anything, because the Hub now shows crew information
- Live vehicle checks from the ncems-checks Worker /fleet/today, grouped Station 51 and Station 52, gauge of in service rigs checked, out of service with the reason. Weekly Rescue and spare checks (Mon Rescue 2, Tue Rescue 7 and 8, Wed Rescue 3, 4 and 5, Thu Rescue 1, Fri M14 and M12) listed as also due today. Needs the Worker to accept the Hub (see Setup)
- Weather from the National Weather Service for the picked station: now, high and low, a plain sentence about rain and freezing, alerts, next 24 hours
- Day of the week duties from the NCEMS / FD13 Weekly Station Duties checklist (6.2025), rig checks moved to Vehicle checks
- Kept: apps.json buttons, notice posting and banner, usage counter, login hint to other apps, haptics, update check (the Wall reloads itself on a new version)
- Coming next: crews on each unit, open shifts and the week, checking off duties and BC added items (need Worker changes)

### Setup (done 11/14)
- ncems-checks Worker 1.6: CLIENT_IDS includes `54eb93f5-05e0-42ca-a49d-f4df05c3331c`, ORIGINS includes `https://hub.northcountryems.org`. New routes GET /fleet/hub, POST /fleet/duty, /fleet/duty/add, /fleet/duty/remove

### v2.4 (10/24/2026)
- New top bar, the same as CG Staff: white bar, house button on the left goes to the top of the Hub (this is the Hub), NCEMS logo, "NCEMS" in black and the app name in green, North Country EMS in gray, and the i button on the right for details. iPhone status bar set to default so the clock shows on the white bar
- Incident Report button now reads "During Duty Incident Report" with "Service related reporting" under it; Facilities and Grounds reads "Buildings and grounds" (apps.json and the backup buttons)
- Changed index.html, apps.json and README.md

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
