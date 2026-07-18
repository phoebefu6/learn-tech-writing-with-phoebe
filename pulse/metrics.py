import csv
from collections import defaultdict
from pathlib import Path

import yaml

CFG = yaml.safe_load(open(Path(__file__).parent / "config.yaml"))


def daily_metrics() -> Path:
    cleaned = Path(CFG["paths"]["cleaned"])
    out_dir = Path(CFG["paths"]["metrics"])
    out_dir.mkdir(parents=True, exist_ok=True)
    days = defaultdict(lambda: {"events": 0, "users": set(), "value": 0.0})
    for f in sorted(cleaned.glob("*.csv")):
        with open(f, newline="") as fh:
            for row in csv.DictReader(fh):
                day = row["ts"][:10]
                days[day]["events"] += 1
                days[day]["users"].add(row["user_id"])
                days[day]["value"] += float(row["value"])
    out = out_dir / "daily_metrics.csv"
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["day", "events", "active_users", "total_value", "alert"])
        for day in sorted(days):
            d = days[day]
            alert = "LOW" if d["events"] < CFG["alerts"]["min_daily_events"] else ""
            w.writerow([day, d["events"], len(d["users"]), f"{d['value']:.2f}", alert])
    return out


if __name__ == "__main__":
    print(daily_metrics())
