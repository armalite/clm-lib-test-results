import json
c=json.load(open('/task/workspace/context.json'))
keep=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
keep.append({'id':'n6','role':'note','body':'R4 logs: auth-svc certificate_expired peer=bank-api continues (round-04/logs/auth-svc.log:3,5,7,20,40,42,55). Slow-query WARNs everywhere = noise. Next: advance to R5.'})
c['entries']=keep
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')