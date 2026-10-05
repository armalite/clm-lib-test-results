import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4','n5')]
e.append({'id':'n6','role':'note','body':'R6: board.md:3 Thread B services now include search-api (cause/status unchanged). Log fmt now JSON. CERT_EXPIRED errors peer=sso.example.net search-api.log:11,14,25,26,35 shipping-svc.log:4,35,40,45,51. No other errors. Next: advance to R7.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))