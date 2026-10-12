import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR8 logs: search-api BOTH 429 tax-provider (round-08/logs/search-api.log:1,12,14,20,25,66) AND config validation failed http.max_inflight=-1 (round-08/logs/search-api.log:2,5,10,26,42) => Thread C = BAD_CONFIG_ROLLOUT via CHG-120 (round-02/changes.md:3), separate from Thread D. Cert errs auth round-08/logs/auth-svc.log:8,61; shipping round-08/logs/shipping-svc.log:50,60. NEXT: advance to R9.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')