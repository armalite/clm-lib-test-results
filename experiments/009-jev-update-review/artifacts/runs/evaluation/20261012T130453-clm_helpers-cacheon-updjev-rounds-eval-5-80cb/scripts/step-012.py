import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
  L=open(f).read().splitlines()
  hits=[(i+1,l[:130]) for i,l in enumerate(L) if re.search(r'ERROR|WARN|expired|pool|disk|429|lag|mem',l,re.I) and 'slow' not in l]
  print(f.split('/')[-1],len(hits))
  for h in hits[:3]+hits[-1:]: print(h)
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4')]
c['entries'][3]['body']+=' R4 logs: auth-svc cert_expired continues (round-04/logs/auth-svc.log:3-55); others clean.'
c['entries'].append({'id':'n5','role':'note','body':'R5: board.md:3 OPEN CAPACITY_REVIEW.'})
json.dump(c,open('/task/workspace/context.json','w'))