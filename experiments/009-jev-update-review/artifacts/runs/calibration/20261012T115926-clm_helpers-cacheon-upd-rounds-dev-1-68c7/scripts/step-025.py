import json,re
d=json.load(open('/task/workspace/context.json'))
n=[e for e in d['entries'] if e['id']=='n1'][0]
n['body']+=' R8: board.md:3 Thread A resolved; board.md:4 Thread B cause revised UPSTREAM_RATE_LIMIT; board.md:5 Thread C notify-worker ongoing cause unknown (likely CHG-120 max_inflight=0); CHG-159 PROPOSED ignore.'
d['entries']=[n]
json.dump(d,open('/task/workspace/context.json','w'))
for i,l in enumerate(open('/task/fixtures/round-08/logs/notify-worker.log'),1):
  if re.search('ERROR|inflight|config',l,re.I): print(i,l.strip()[:160])