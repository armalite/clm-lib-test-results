import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n8','role':'note','body':'R8: board Thread A resolved (round-08/board.md:3); Thread B cause revised UPSTREAM_RATE_LIMIT (round-08/board.md:4), still ongoing; Thread C opened notify-worker ongoing, cause unknown (round-08/board.md:5). notify-worker ERROR config validation failed http.max_inflight=0 (round-08/logs/notify-worker.log:5) -> BAD_CONFIG_ROLLOUT via CHG-120 (round-02/changes.md:4). 429s continue checkout(:1,6) payments(:2). CHG-159 PROPOSED only.'})
json.dump(c,open('/task/workspace/context.json','w'))
for i,l in enumerate(open('/task/fixtures/round-08/logs/notify-worker.log'),1):
  if 'ERROR' in l:print(i,end=' ')