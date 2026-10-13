import json
c=json.load(open('/task/workspace/context.json'))
keep=('n1','n2','n3','n6','n4','n5')
E=[e for e in c['entries'] if e['id'] in keep]
E.append({'id':'n8','role':'note','body':'Thread C shipping-svc ongoing BAD_CONFIG_ROLLOUT: r09 board.md:4 opened, r10 board.md:4 still restarting; r09 shipping-svc.log:1, r10 shipping-svc.log:1,17; r11 shipping-svc.log:5-18 config validation failed db.pool_max=-4 (CHG-120 r02 changes.md:4). R11 board empty. Next: advance to R12.'})
c['entries']=E
json.dump(c,open('/task/workspace/context.json','w'))