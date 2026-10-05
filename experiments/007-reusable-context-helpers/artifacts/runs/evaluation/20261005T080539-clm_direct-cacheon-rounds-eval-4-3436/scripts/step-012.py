import json,re
b='/task/fixtures/round-04/logs/'
for f in ['auth-svc.log','shipping-svc.log']:
    L=open(b+f).read().splitlines()
    m=[i+1 for i,l in enumerate(L) if re.search('memory|OOM|restart|heap',l,re.I)]
    r=[i+1 for i,l in enumerate(L) if '429' in l]
    c=[i+1 for i,l in enumerate(L) if 'miss storm' in l]
    print(f,'mem',m[:10],'429',r[:12],'storm',c[:8])
c=json.load(open('/task/workspace/context.json'))
keep=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
keep.append({'id':'n4','role':'note','body':'R4: board.md:3 Thread B opened MEMORY_LEAK auth-svc ongoing (verify against logs); board.md:4 follow-up OPEN VENDOR_TICKET. 429 from upstream=tax-provider in auth-svc.log:12,16 and shipping-svc.log:5,21,28,29 (UPSTREAM_RATE_LIMIT, not yet on board). Cache miss storm continues auth-svc.log:1,2. Pool WARNs continue inventory-svc.log:3-23, notify-worker.log:11-42. search-api quiet.'})
c['entries']=keep
json.dump(c,open('/task/workspace/context.json','w'))