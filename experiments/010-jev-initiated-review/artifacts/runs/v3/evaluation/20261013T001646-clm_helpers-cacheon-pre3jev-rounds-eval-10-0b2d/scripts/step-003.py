import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Round 1: board empty; changes.md exists (not yet read). Logs (shipping, checkout, auth, inventory, search) only show background WARN slow query ms~200-450, no errors. Baseline noise. Next: read round-01/changes.md, then advance.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-01/changes.md').read()[:1500])