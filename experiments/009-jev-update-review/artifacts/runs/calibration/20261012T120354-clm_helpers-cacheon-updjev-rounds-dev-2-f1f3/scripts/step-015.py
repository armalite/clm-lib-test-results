import json,re,os
b='/task/fixtures/round-06/logs/'
for f in sorted(os.listdir(b)):
  L=open(b+f).read().splitlines()
  hits=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|SERVFAIL|certificate|429|pool|max_inflight|OOM|disk|lag',l,re.I)]
  print(f,len(hits),hits[:12])
  if hits:print(' ',L[hits[0]-1][:120])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n6','role':'note','body':'R6: board.md:3 RUNBOOK_UPDATE OPEN. changes.md:3 CHG-144 log sampling (noise).'})
json.dump(c,open('/task/workspace/context.json','w'))