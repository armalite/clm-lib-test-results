import re,json
L=open('/task/fixtures/round-08/logs/search-api.log').read().splitlines()
for i,l in enumerate(L):
    if not re.search(r'INFO|slow query',l):print(i+1,l[60:200])
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'].startswith('n')]
e.append({'id':'n8','role':'note','body':'R8: round-08/board.md:3 Thread A resolved; :4 Thread B mitigated; :5 Thread C opened search-api failures cause unknown ongoing; :6 DATA_BACKFILL OPEN; :7 VENDOR_TICKET CLOSED. Logs: auth-svc.log:8,61 and shipping-svc.log:50,60 cert_expired few (tapering); search-api.log:1-72 15 non-INFO lines (429 tax-provider etc). R8 next: advance.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))