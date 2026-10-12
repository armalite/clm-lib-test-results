import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if not e['id'].startswith(('s26','s27'))]
c['entries'].append({'id':'n10','role':'note','body':'R10 board: B adds payments-svc (round-10/board.md:3); C opened notify-worker request failures cause unknown ongoing (round-10/board.md:4) - suspect CHG-113 BAD_CONFIG; Follow-ups OPEN DATA_BACKFILL (round-10/board.md:5), POSTMORTEM_DRAFT (round-10/board.md:6). CHG-173 irrelevant.'})
json.dump(c,open('/task/workspace/context.json','w'))
for i,l in enumerate(open('/task/fixtures/round-10/logs/notify-worker.log'),1):
  if 'pool' in l.lower() or 'ERROR' in l or 'config' in l.lower(): print(i,l.rstrip()[:160])