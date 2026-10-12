import json,re
for s in ['search-api','auth-svc','shipping-svc','checkout-api','inventory-svc']:
    L=open(f'/task/fixtures/round-07/logs/{s}.log').read().splitlines()
    h=[(i+1,l[:150]) for i,l in enumerate(L) if re.search(r'429|ERROR|cert|SERVFAIL|max_inflight',l,re.I)]
    print(s,len(h));[print(x) for x in h[:4]]
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]
n['body']+='\nR7: board.md:3 Thread B cause revised CERT_EXPIRED; board.md:4 Thread D UPSTREAM_RATE_LIMIT search-api ongoing (verify vs CHG-120 BAD_CONFIG).'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))