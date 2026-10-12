import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n7','role':'note','body':'R6 logs: ledger-svc heap high round-06/logs/ledger-svc.log:2,6,14,35,45,52 (MEMORY_LEAK evidence). Log scan keywords: heap/rss/429/err. Next: advance to R7.'})
json.dump(c,open('/task/workspace/context.json','w'))