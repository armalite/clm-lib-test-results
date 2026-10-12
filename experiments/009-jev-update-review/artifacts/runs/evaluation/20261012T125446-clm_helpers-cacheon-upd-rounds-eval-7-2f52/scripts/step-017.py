import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4','n5')]
c['entries'].append({'id':'n6','role':'note','body':'R6: board.md:3 Thread A mitigated. changes.md:3 CHG-150 APPLIED mitigation thread A shipping-svc. Logs R6: 429 stopped (search/shipping 0 hits). checkout-api.log disk used_pct 91-98 lines 1,11,31,34 (DISK_PRESSURE continues). R6 scanned; next: advance.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')