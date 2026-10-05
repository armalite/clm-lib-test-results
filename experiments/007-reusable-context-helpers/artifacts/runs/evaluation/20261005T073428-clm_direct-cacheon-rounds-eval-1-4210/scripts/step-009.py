import json
p='/task/workspace/context.json'
d=json.load(open(p))
n=[e for e in d['entries'] if e['id']=='notes'][0]['body']
n+="\nR3: board empty (no changes). changes.md:3 CHG-124 PROPOSED only. Logs: slow query WARN noise all services; 13 lag lines (not yet checked trend). Next: check r03 lag values then advance."
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open(p,'w'))
import re
for f in ['payments-svc','ledger-svc']:
  for i,l in enumerate(open(f'/task/fixtures/round-03/logs/{f}.log'),1):
    if 'lag' in l:print(f,i,l.strip()[-60:])