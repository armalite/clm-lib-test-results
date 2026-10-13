import json
c=json.load(open('/task/workspace/context.json'))
keep=('n1','n2','n3','n6')
E=[e for e in c['entries'] if e['id'] in keep]
E.append({'id':'n4','role':'note','body':'Thread B MEMORY_LEAK inventory-svc+checkout-api: r03 board.md:4; r07 board.md:3 cause; r09 board.md:3 adds checkout-api; r10 board.md:3 MITIGATED. heap r03 inventory-svc.log 4-63.'})
E.append({'id':'n5','role':'note','body':'Thread D (notify cache stampede) CLOSED false alarm r10 board.md:5 -> exclude.'})
E.append({'id':'n8','role':'note','body':'Thread C shipping-svc ongoing: r09 board.md:4 opened, r10 board.md:4 still restarting; r09 shipping-svc.log:1, r10 shipping-svc.log:1,17 config validation failed db.pool_max=-4 -> BAD_CONFIG_ROLLOUT (CHG-120 r02 changes.md:4). r10 CHG-170 log sampling irrelevant. Next: advance to R11.'})
c['entries']=E
json.dump(c,open('/task/workspace/context.json','w'))