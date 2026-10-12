import json,re,collections
b='/task/fixtures/round-08/logs/search-api.log'
C=collections.Counter()
for i,l in enumerate(open(b),1):
  if re.search('ERROR|WARN',l):
    try:d=json.loads(l);C[(d.get('level'),d.get('msg'),d.get('upstream'),d.get('pod'))]+=1
    except:C[l[:120]]+=1
for k,v in C.items():print(v,k)
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]['body']+'\nR8: board.md:3 Thread A RESOLVED; board.md:4 Thread B MITIGATED; board.md:5 Thread C search-api pod failures cause unknown ongoing; board.md:6 OPEN DATA_BACKFILL; board.md:7 CLOSED VENDOR_TICKET. search-api.log 429 tax-provider lines 1-72 (15). CERT errs few: auth-svc.log:8,61 shipping-svc.log:50,60. checkout/inventory 0.'
c['entries']=[{'id':'notes','role':'note','body':n}]
json.dump(c,open('/task/workspace/context.json','w'))