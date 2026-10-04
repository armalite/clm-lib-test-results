import json
p='/task/workspace/context.json'
d={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1: deploy 8.26.3-35fd stage-1/deploy/deploys.log:5. Release notes stage-1/deploy/release-notes-8.26.3-35fd.md:15 db.pool.max_size 60->10 (:11 ledger timeout 800). Stage2: stage-2/deploy/changes.log:2 CHG-5204 APPLIED ledger timeout 3500 (fixed). Now db pool exhausted 10/10 e.g. stage-2/logs/catalog-api.log:224. Hypothesis DB_POOL_EXHAUSTED value 10. Next: advance to stage 3.'}]}
json.dump(d,open(p,'w'))