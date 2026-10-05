import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n8','role':'note','body':'R8: board empty. CHG-156 APPLIED log sampling only. CERT_EXPIRED partner-gw continues (round-08/logs/inventory-svc.log:6,16). DNS SERVFAIL continues ledger (round-08/logs/ledger-svc.log:2,13) pricing (round-08/logs/pricing-svc.log:4,14). Next: advance to R9.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')