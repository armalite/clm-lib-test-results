import json,re
b='/task/fixtures/round-07/logs/'
for s in ['search-api','shipping-svc']:
  L=open(b+s+'.log').read().splitlines()
  h=[i for i,l in enumerate(L,1) if re.search(r'429"|upstream returned|certificate_expired',l)]
  print(s,h)
c=json.load(open('/task/workspace/context.json'))
keep=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6')]
keep.append({'id':'n7','role':'note','body':'R7: board.md:3 Thread B cause revised CERT_EXPIRED. board.md:4 Thread D UPSTREAM_RATE_LIMIT search-api ongoing (tax-provider 429; see lines printed in s21). CERT errs round-07/logs/auth-svc.log:1-64. No errs checkout/inventory. Note shipping 429 hits may be slow-query ms noise.'})
c['entries']=keep
json.dump(c,open('/task/workspace/context.json','w'))