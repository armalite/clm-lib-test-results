import json
c=json.load(open('/task/workspace/context.json'))
keep=[e for e in c['entries'] if e['id'] in ('n1','n2','n3','n4','n5','n6','n7','n8')]
keep.append({'id':'n9','role':'note','body':'R9: round-09/board.md:3 Thread C pods restarting, investigating. R10: board empty; round-10/changes.md:3 CHG-174 APPLIED retry budget (unrelated). search-api still config validation failed max_inflight=-1 round-10/logs/search-api.log:1,15. Ready for final.'})
json.dump({'format':'clm-context/v1','entries':keep},open('/task/workspace/context.json','w'))
print('ok')