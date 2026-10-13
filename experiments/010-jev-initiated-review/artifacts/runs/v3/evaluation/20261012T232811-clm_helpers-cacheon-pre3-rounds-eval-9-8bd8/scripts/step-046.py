import json
p='/task/workspace/context.json'
e=json.load(open(p))['entries']
keep=[x for x in e if x['id'] in ('n2','n4','n6','n7','n8')]
keep.append({'id':'n9','role':'note','body':'Round9: board only Thread C note pods restarting (round-09/board.md:3). search-api config validation http.max_inflight ERROR round-09/logs/search-api.log:2,14,18,20,23,24,33. disk WARN notify-worker:4,8 shipping-svc:8,13. Next: advance to round 10.'})
json.dump({'format':'clm-context/v1','entries':keep},open(p,'w'))
print('ok')