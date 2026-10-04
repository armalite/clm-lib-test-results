import json,re,collections
b='/task/fixtures/stage-1/'
c=collections.Counter();first={}
for f in ['logs/edge-gw.log','logs/returns-svc.log']:
  for i,l in enumerate(open(b+f),1):
    if 'ERROR' in l:
      k=f+' '+re.sub(r'\d+','N',l[50:140])
      c[k]+=1
      first.setdefault(k,(i,l.strip()[:220]))
for k,v in c.most_common(12):print(v,first[k])
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1: deploys.log:3 returns-svc 6.33.4-cb27 at 08:16:14. release-notes-6.33.4-cb27.md:5 tax-engine timeout_ms 2500->750; :19 db.pool.max_size 48->10. config yaml:7 timeout 2500, :11 pool 48. oncall suspects tax-engine timeout (informal). Noise: gc pauses, disk 70%, dns retry ok, tls expires 34d.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))