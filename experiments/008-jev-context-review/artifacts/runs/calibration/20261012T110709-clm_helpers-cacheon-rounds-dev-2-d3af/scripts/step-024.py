import re,json
L=open('/task/fixtures/round-08/logs/search-api.log').read().splitlines()
from collections import Counter
c=Counter()
for i,l in enumerate(L):
    if 'ERROR' in l:
        try:c[json.loads(l).get('msg')]+=1
        except:c[l[:80]]+=1
print(c)
p='/task/workspace/context.json'
n=json.load(open(p))['entries'][0]['body']
n+=' R8: board round-08/board.md:3 Thread A resolved; :4 Thread B mitigated; :5 Thread C search-api failures unknown ongoing; :6 DATA_BACKFILL OPEN; :7 VENDOR_TICKET CLOSED. CERT errs few: round-08/logs/auth-svc.log:8-61 (2), round-08/logs/shipping-svc.log:50-60 (2). search-api 429 tax-provider round-08/logs/search-api.log:1-72 (15). checkout/inventory none.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open(p,'w'))