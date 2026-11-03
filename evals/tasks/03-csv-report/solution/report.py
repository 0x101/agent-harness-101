import csv, json
from collections import defaultdict

agg = defaultdict(lambda: {"orders": 0, "total": 0.0})
for r in csv.DictReader(open("sales.csv")):
    agg[r["region"]]["orders"] += 1
    agg[r["region"]]["total"] += float(r["amount"])
for v in agg.values():
    v["total"] = round(v["total"], 2)
json.dump(agg, open("summary.json", "w"), indent=2, sort_keys=True)
print(max(agg, key=lambda k: agg[k]["total"]))
