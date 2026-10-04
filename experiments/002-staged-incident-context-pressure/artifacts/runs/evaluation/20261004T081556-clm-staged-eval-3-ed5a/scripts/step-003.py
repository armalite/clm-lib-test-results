import json,re,collections
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1: deploy returns-svc 6.33.4-cb27 at stage-1/deploy/deploys.log:3 (08:16). Release notes stage-1/deploy/release-notes-6.33.4-cb27.md:5 tax-engine timeout_ms 2500->750; :19 db pool max_size 48->10. edge-gw 503 upstream timeout e.g. stage-1/logs/edge-gw.log:76. returns-svc.log ERRORs: tax-engine timed out (first ~line 161). oncall suspects timeout.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))
b='/task/fixtures/stage-1/logs/returns-svc.log'
c=collections.Counter()
for i,l in enumerate(open(b),1):
 if re.search('pool|tax-engine.*(ok|latency|ms)',l) and 'ERROR' not in l:c[re.sub(r'\d+','N',l[40:])[:80]]+=1
for k,v in c.most_common(6):print(v,k)
for i,l in enumerate(open(b),1):
 if 'timed out' in l and i<200:print(i,l[40:140]);break
