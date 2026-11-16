#!/usr/bin/env python3
"""NCEMS Training Calendar: Excel "Event List" -> training-events.json

Usage:  python3 excel_to_training_json.py NCEMS_Training_Calendar.xlsx training-events.json
Needs:  pip install openpyxl

Reads the "Event List" tab (row 1 = headers):
  Date | Day | Event | Time | Who / notes | Type (optional, recommended)
One row = one day. Two things on the same day = two rows.
Writes {"types": {...}, "events": [...]} that the Hub (index.html) and training.html read.
If Type is blank it is guessed from the Event text (ACLS, PEAC, vacation, holiday names...).
Stops with a clear message instead of writing a bad file.
"""
import json, sys, datetime, re

TYPES = {
    "acls":       {"label": "ACLS",        "bg": "#F4CCCC", "text": "#990000"},
    "pals":       {"label": "PALS",        "bg": "#E2F0D9", "text": "#375623"},
    "peac":       {"label": "PEAC",        "bg": "#DCE6F5", "text": "#1F3864"},
    "advcardiac": {"label": "Adv Cardiac", "bg": "#FCE4D6", "text": "#843C0C"},
    "otep":       {"label": "OTEP",        "bg": "#E4DFEC", "text": "#5B1A86"},
    "pcep":       {"label": "PCEP",        "bg": "#DDEBF7", "text": "#2E5090"},
    "ftep":       {"label": "FTEP",        "bg": "#FFF2CC", "text": "#7F6000"},
    "off":        {"label": "No training", "bg": "#D9D9D9", "text": "#404040"},
    "holiday":    {"label": "Holiday",     "bg": "#FFF2CC", "text": "#7F6000"},
}
HOLIDAYS = ["new year", "martin luther king", "presidents", "memorial day", "juneteenth", "independence",
            "labor day", "veterans", "thanksgiving", "christmas"]

def guess_type(text):
    t = text.lower()
    if "pals" in t: return "pals"
    if "adv cardiac" in t or "advanced cardiac" in t: return "advcardiac"
    if "acls" in t: return "acls"
    if "peac" in t: return "peac"
    if "otep" in t: return "otep"
    if "pcep" in t: return "pcep"
    if "ftep" in t: return "ftep"
    if "vacation" in t or "no training" in t: return "off"
    if any(h in t for h in HOLIDAYS): return "holiday"
    return ""

def to_ymd(v, row):
    if isinstance(v, datetime.datetime): return v.date().isoformat()
    if isinstance(v, datetime.date): return v.isoformat()
    s = str(v or "").strip()
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{4})$", s)
    if m: return datetime.date(int(m[3]), int(m[1]), int(m[2])).isoformat()
    if re.match(r"^\d{4}-\d{2}-\d{2}$", s): return s
    sys.exit(f"Row {row}: the date '{s}' is not a date. Use MM/DD/YYYY.")

def main(src, out):
    from openpyxl import load_workbook
    wb = load_workbook(src, data_only=True)
    if "Event List" not in wb.sheetnames: sys.exit("No 'Event List' tab in the workbook.")
    ws = wb["Event List"]
    rows = list(ws.iter_rows(values_only=True))
    head = [str(h or "").strip().lower() for h in rows[0]]
    def col(*names):
        for n in names:
            for i, h in enumerate(head):
                if h.startswith(n): return i
        return None
    c_date, c_event, c_time, c_notes, c_type = col("date"), col("event"), col("time"), col("who", "notes"), col("type")
    if c_date is None or c_event is None: sys.exit("Event List needs a Date column and an Event column in row 1.")
    events, problems = [], []
    for r, vals in enumerate(rows[1:], start=2):
        if not vals or all(v in (None, "") for v in vals): continue
        title = str(vals[c_event] or "").strip()
        if not title: problems.append(f"Row {r}: no Event text"); continue
        typ = str(vals[c_type] or "").strip().lower() if c_type is not None else ""
        typ = typ or guess_type(title)
        if typ not in TYPES: problems.append(f"Row {r}: type '{typ or '(blank)'}' for '{title}'. Use one of: {', '.join(TYPES)}"); continue
        e = {"title": title, "type": typ, "date": to_ymd(vals[c_date], r)}
        if c_time is not None and vals[c_time]: e["time"] = str(vals[c_time]).strip()
        if c_notes is not None and vals[c_notes]: e["notes"] = str(vals[c_notes]).strip()
        events.append(e)
    if problems: sys.exit("Not written. Fix these rows first:\n  " + "\n  ".join(problems))
    events.sort(key=lambda e: (e["date"], e["title"]))
    with open(out, "w", encoding="utf-8") as f:
        f.write('{\n  "types": {\n')
        f.write(",\n".join(f'    {json.dumps(k)}: {json.dumps(v, ensure_ascii=False)}' for k, v in TYPES.items()))
        f.write('\n  },\n  "events": [\n')
        f.write(",\n".join("    " + json.dumps(e, ensure_ascii=False) for e in events))
        f.write("\n  ]\n}\n")
    json.load(open(out, encoding="utf-8"))  # proves the file is valid JSON
    print(f"Wrote {out}: {len(events)} events, {events[0]['date'] if events else '-'} to {events[-1]['date'] if events else '-'}")

if __name__ == "__main__":
    if len(sys.argv) != 3: sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
