import json,re,glob
out=[]
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-04/'+f),1):
    if l.strip() and not l.startswith('#'):out.append(f'{f}:{i} {l.strip()}')
for p in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  d={}
  for i,l in enumerate(open(p),1):
    if 'slow query' in l: continue
    k=re.sub(r'\d+','#',l.strip())[20:110]
    d.setdefault(k,[]).append(i)
  for k,v in d.items():out.append(f"{p.split('/')[-1]} {v[:6]} n={len(v)} {k}")
s='\n'.join(out)[:2500]
print(s)
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2')]
e.append({'id':'n3','role':'note','body':'R3: board Thread A CERT_EXPIRED search-api + inventory-svc ongoing (round-03/board.md:3); Follow-up OPEN RUNBOOK_UPDATE (:4), POSTMORTEM_DRAFT (:5). CHG-126 APPLIED TLS ticket rotation hourly (round-03/changes.md:3). R3 logs slow-query noise only.'})
e.append({'id':'n4','role':'note','body':'R4 raw:\n'+s})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))