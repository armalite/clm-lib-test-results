import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6','n7')]
c['entries'].append({'id':'n8','role':'note','body':'R8: board.md:3 Thread A resolved; board.md:4 Thread B mitigated; board.md:5 Thread C opened search-api failures cause unknown ongoing (logs: config validation failed cache.ttl_s=-1 build 8.23.7 search-api.log:24,34,36,41,54,56,60,78,82,84 => BAD_CONFIG_ROLLOUT from CHG-113); board.md:6 follow-up OPEN CAPACITY_REVIEW. 429 auth-svc.log:29,40; shipping-svc.log:41,42. Next: advance.'})
json.dump(c,open('/task/workspace/context.json','w'))