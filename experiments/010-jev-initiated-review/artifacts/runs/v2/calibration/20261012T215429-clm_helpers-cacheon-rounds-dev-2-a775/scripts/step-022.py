import json
b='/task/fixtures/round-07/'
L=open(b+'logs/search-api.log').read().splitlines()
print(L[3][:200])
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
n['body']+=' R7: board.md:3 Thread B revised CERT_EXPIRED; board.md:4 Thread D UPSTREAM_RATE_LIMIT search-api ongoing, search-api.log:4,5 429 upstream tax-. CERT auth-svc.log:1,16 shipping-svc.log:10,11. No DNS. Round 7 reviewed; next: advance.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))