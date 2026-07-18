import csv
from datetime import datetime, timezone
from pathlib import Path

import yaml

CFG = yaml.safe_load(open(Path(__file__).parent / "config.yaml"))

VALID_TYPES = set(CFG["events"]["valid_types"])


def clean() -> int:
    staged = Path(CFG["paths"]["staged"])
    cleaned = Path(CFG["paths"]["cleaned"])
    cleaned.mkdir(parents=True, exist_ok=True)
    seen: set[str] = set()
    kept = 0
    for f in sorted(staged.glob("*.csv")):
        rows = []
        with open(f, newline="") as fh:
            for row in csv.DictReader(fh):
                if row["event_id"] in seen:
                    continue
                if row["event_type"] not in VALID_TYPES:
                    continue
                try:
                    ts = datetime.fromisoformat(row["ts"])
                    if ts.tzinfo is None:
                        ts = ts.replace(tzinfo=timezone.utc)
                    row["ts"] = ts.astimezone(timezone.utc).isoformat()
                    row["value"] = f"{float(row['value']):.2f}"
                except ValueError:
                    continue
                seen.add(row["event_id"])
                rows.append(row)
        with open(cleaned / f.name, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()) if rows else [])
            if rows:
                w.writeheader()
                w.writerows(rows)
        kept += len(rows)
    return kept


if __name__ == "__main__":
    print(clean())
