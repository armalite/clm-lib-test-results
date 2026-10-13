import json,collections
t=open('/task/workspace/spill/s8.obs.txt').read().splitlines()
c=collections.Counter()
ex={}
for l in t:
  p=l.split()
  if len(p)>5:
    k=p[0]+' '+' '.join(p[4:8])
    c[k]+=1; ex.setdefault(k,p[0]+':'+p[1])
for k,v in c.most_common(15):print(v,ex[k],k[:110])
n1=json.load(open('/task/workspace/context.json'))['entries'][0]
n2={'id':'n2','role':'note','body':'Round2: board lines3-4 follow-ups OPEN VENDOR_TICKET, POSTMORTEM_DRAFT (round-02/board.md:3-4). CHG-116 APPLIED log sampling health 1% (benign). pricing-svc has "upstream returned" lines (lines 4,6,12,21; likely 429 UPSTREAM_RATE_LIMIT). Non-slow-query lines spilled at spill/s8.obs.txt.'}
json.dump({'format':'clm-context/v1','entries':[n1,n2]},open('/task/workspace/context.json','w'))