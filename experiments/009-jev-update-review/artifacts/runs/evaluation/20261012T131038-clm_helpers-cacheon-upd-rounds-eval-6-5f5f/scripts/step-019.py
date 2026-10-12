import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n9','role':'note','body':'R7 logs: ledger-svc heap high round-07/logs/ledger-svc.log:7,10,16,23,26,60 (MEMORY_LEAK ongoing). Next: advance to R8.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')