import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'].startswith('n')]
e.append({'id':'n9','role':'note','body':'R8b: search-api.log round-08 lines 2,5,10,26,42,44,59,68,72 config validation failed http.max_inflight=-1 (Thread C real cause BAD_CONFIG_ROLLOUT, cite round-02/changes.md:3 CHG-120); 429 tax-provider lines 1,12,14,20,25,66 (Thread D). R8 done; next: advance.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))