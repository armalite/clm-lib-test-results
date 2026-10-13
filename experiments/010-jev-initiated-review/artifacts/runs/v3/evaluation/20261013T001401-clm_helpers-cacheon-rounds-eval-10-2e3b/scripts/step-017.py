import json
d=json.load(open('/task/workspace/context.json'))
b=d['entries'][0]['body']
b=b.replace('\nTool:','\nR6: board.md:3 Thread A mitigated; :4 Thread B revised UPSTREAM_RATE_LIMIT; :5 FU OPEN ALERT_TUNING. changes:3 CHG-150 APPLIED mitigation A auth-svc. (scan.py printed INFO lines in R6 - log format may have changed; check levels.)\nTool:')
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':b}]},open('/task/workspace/context.json','w'))
import glob,re
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
  L=open(f).read().splitlines()
  hits=[i+1 for i,l in enumerate(L) if not re.search(r'INFO|info',l)]
  print(f.split('/')[-1],len(hits),hits[:3],hits[-1:] if hits else '')
  if hits: print(L[hits[0]-1][:200])