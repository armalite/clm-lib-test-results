import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  L=open(f).read().splitlines()
  hits=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|WARN|exhaust|expired|disk|pool',l,re.I)]
  print(f.split('/')[-1],len(hits),hits[:3],hits[-1:] if hits else '')
  if hits: print('  ',L[hits[0]-1][:200])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
c['entries'].append({'id':'n7','role':'note','body':'R7: board.md:3 Thread A (DISK search+shipping) RESOLVED; :4 Thread B cause revised to CERT_EXPIRED (auth-svc); :5 OPEN ALERT_TUNING.'})
json.dump(c,open('/task/workspace/context.json','w'))