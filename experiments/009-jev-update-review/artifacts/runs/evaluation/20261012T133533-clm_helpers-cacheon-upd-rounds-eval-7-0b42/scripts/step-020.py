import json,subprocess
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
c['entries'][0]['body']+=' R8: Thread B services +payments-svc (round-08/board.md:3); OPEN RUNBOOK_UPDATE (r8 board.md:4).'
json.dump(c,open('/task/workspace/context.json','w'))
import glob
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if any(k in l.lower() for k in ['disk','429','pool','cache','error']): print(f.split('/')[-1],i,l.strip()[:150])
