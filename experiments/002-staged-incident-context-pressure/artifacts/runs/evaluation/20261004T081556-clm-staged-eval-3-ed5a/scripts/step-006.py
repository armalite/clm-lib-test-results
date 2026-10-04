import json
ctx=json.load(open('/task/workspace/context.json'))
keep=[e for e in ctx['entries'] if e['id']=='n1']
keep.append({'id':'n2','role':'note','body':'Stage2: stage-2/deploy/changes.log:1 CHG-5395 APPLIED tax timeout 4000. New symptom db pool exhausted N/10 stage-2/logs/returns-svc.log:235; edge 503 stage-2/logs/edge-gw.log:94. Pool max_size 10 from release notes stage-1/deploy/release-notes-6.33.4-cb27.md:19 (yaml says 48 but overridden). Hypothesis DB_POOL_EXHAUSTED. Next: advance to stage 3.'})
ctx['entries']=keep
json.dump(ctx,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/stage-2/logs/returns-svc.log').readlines()[234][:200])