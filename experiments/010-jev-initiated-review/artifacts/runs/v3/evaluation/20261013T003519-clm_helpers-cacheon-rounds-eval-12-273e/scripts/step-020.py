import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'].startswith('n')]
e.append({'id':'n7','role':'note','body':'R7: board.md:3 Thread B services +checkout-api, cause/status unchanged. CHG-152 PROPOSED ignore. 429 tax-provider checkout-api.log:4-49, ledger-svc.log:13-77. Next: advance R8.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')