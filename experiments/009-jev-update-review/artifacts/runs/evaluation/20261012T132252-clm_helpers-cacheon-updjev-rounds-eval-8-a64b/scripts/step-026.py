import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if not e['id'].startswith(('s24','s25'))]
for e in c['entries']:
  if e['id']=='n9': e['body']+=' R9 board: Follow-up OPEN RUNBOOK_UPDATE (round-09/board.md:3).'
json.dump(c,open('/task/workspace/context.json','w'))
for i,l in enumerate(open('/task/fixtures/round-09/logs/notify-worker.log'),1):
  if 'pool' in l.lower() or 'ERROR' in l: print(i,l.rstrip()[:150])