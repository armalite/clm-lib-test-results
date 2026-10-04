import json
b='/task/fixtures/stage-2/logs/payments-api.log'
L=open(b).readlines()
x=[i for i,l in enumerate(L,1) if 'db pool exhausted' in l]
print(x[0],x[-1],L[x[0]-1].strip()[:170])
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1: RN stage-1/deploy/release-notes-5.36.1-f33d.md:13 risk timeout 2500->800; :16 db pool 60->14. deploys.log:4. s1 payments-api.log:179 risk timeout; :206 pool 14/14. yaml:11 pool 60.'},{'id':'n2','role':'note','body':'Stage2: changes.log:2 CHG-5341 APPLIED timeout=4000 (fixed timeouts). New errors: db pool exhausted (110) in stage-2/logs/payments-api.log first line %d. Pool effective 14 from build. Next: advance to stage 3.'%x[0]}]}
json.dump(ctx,open('/task/workspace/context.json','w'))