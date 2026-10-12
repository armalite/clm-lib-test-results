import json
d=json.load(open('/task/workspace/context.json'))
d['entries']=[e for e in d['entries'] if e['id']=='n1']
d['entries'][0]['body']+=' r10 ledger errors lines 12,13,15,18; checkout/payments no disk warns r10. Round 10 done; next: advance.'
json.dump(d,open('/task/workspace/context.json','w'))
print('ok')