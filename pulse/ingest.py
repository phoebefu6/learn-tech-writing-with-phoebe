import csv
import sys
from pathlib import Path

import yaml

CFG = yaml.safe_load(open(Path(__file__).parent / "config.yaml"))

REQUIRED = ["event_id", "user_id", "event_type", "ts", "value"]


def ingest(raw_dir: str | None = None) -> int:
    raw = Path(raw_dir or CFG["paths"]["raw"])
    staged = Path(CFG["paths"]["staged"])
    staged.mkdir(parents=True, exist_ok=True)
    n = 0
    for f in sorted(raw.glob("*.csv")):
        rows = []
        with open(f, newline="") as fh:
            reader = csv.DictReader(fh)
            if reader.fieldnames is None or [c for c in REQUIRED if c not in reader.fieldnames]:
                print(f"skip {f.name}: bad header", file=sys.stderr)
                continue
            for row in reader:
                if not row["event_id"] or not row["ts"]:
                    continue
                rows.append({k: row[k] for k in REQUIRED})
        out = staged / f.name
        with open(out, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=REQUIRED)
            w.writeheader()
            w.writerows(rows)
        n += len(rows)
    return n


if __name__ == "__main__":
    print(ingest(sys.argv[1] if len(sys.argv) > 1 else None))
