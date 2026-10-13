import json
c=json.load(open('/task/workspace/context.json'))
E={e['id']:e for e in c['entries']}
E['n9']['body']='Round9: board.md:3 Thread C note: failing pods still restarting, investigation continues (still ongoing, cause unknown on board). search-api config validation failed http.max_inflight round-09/logs/search-api.log:2,14,18,20,23,24,33. Next: advance to round 10.'
c['entries']=[E[k] for k in ['n1','n2','n3','n4','n5','n6','n7','n8','n9']]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')