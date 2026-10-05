import json
b='/task/fixtures/round-10/logs/'
for n,ls in [('search-api.log',[1,4,7,8,20]),('auth-svc.log',[10,17]),('shipping-svc.log',[3,60])]:
  L=open(b+n).readlines()
  for i in ls:print(n,i,L[i-1].rstrip()[:110])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
c['entries'].append({'id':'n11','role':'note','body':'R10: round-10/board.md:3 Thread D false alarm (drop); :4 DATA_BACKFILL CLOSED. changes CHG-175 noise. search-api.log 9 hits [1,4,7,8,20,30,50,54,60]; auth-svc.log:10,17 shipping-svc.log:3,60 cert. Next: advance to R11.'})
json.dump(c,open('/task/workspace/context.json','w'))