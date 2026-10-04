import json,re
b='/task/fixtures/stage-1/'
L=open(b+'logs/returns-svc.log').read().splitlines()
lat=[int(m.group(1)) for l in L for m in [re.search(r'tax-engine.*?latency[^0-9]*(\d+)',l)] if m]
print(len(lat),sorted(lat)[len(lat)//2] if lat else None)
for i,l in enumerate(L,1):
  if 'pool' in l.lower() and i<900: print(i,l[:160]);break
print(sum('pool' in l.lower() for l in L))
print(L[300][:200])
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1: deploys.log:3 returns-svc 6.33.4-cb27 at 08:16:14. release-notes-6.33.4-cb27.md:5 tax-engine timeout_ms 2500->750; :19 db.pool.max_size 48->10. config yaml:7 timeout 2500, :11 pool 48. Symptom returns-svc.log:161-179 tax-engine timed out after 750ms (many). Noise: gc, disk, dns, tls.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))