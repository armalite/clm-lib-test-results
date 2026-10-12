import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
for e in c['entries']:
  if e['id']=='n7': e['body']=e['body'].replace('Thread D UPSTREAM_RATE_LIMIT search-api ongoing','Thread D UPSTREAM_RATE_LIMIT search-api (CLOSED false alarm R10 board.md:3)')
c['entries'].append({'id':'n10','role':'note','body':'R10: board.md:3 Thread D closed FALSE ALARM (drop UPSTREAM_RATE_LIMIT). board.md:4 DATA_BACKFILL CLOSED. changes.md:3 CHG-175 noise. Open follow-ups now: ALERT_TUNING, RUNBOOK_UPDATE. Incidents: A DNS resolved, B CERT mitigated, C BAD_CONFIG search-api ongoing. Next: advance R11.'})
json.dump(c,open('/task/workspace/context.json','w'))