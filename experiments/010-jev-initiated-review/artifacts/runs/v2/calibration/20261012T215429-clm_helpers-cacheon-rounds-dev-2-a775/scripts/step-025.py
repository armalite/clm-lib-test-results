import json,os
b='/task/fixtures/round-08/'
print(os.path.exists(b+'changes.md') and open(b+'changes.md').read())
L=open(b+'logs/search-api.log').read().splitlines()
for i,l in enumerate(L,1):
  if 'ERROR' in l and '429' not in l:print(i,l[:200])
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
n['body']+=' R8: board.md:3 Thread A resolved; :4 Thread B mitigated; :5 Thread C search-api pod failures ongoing cause unknown; :6 OPEN DATA_BACKFILL; :7 CLOSED VENDOR_TICKET. search-api 429 tax-provider search-api.log:1,2. CERT auth-svc.log:8,61 shipping-svc.log:50,60.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))