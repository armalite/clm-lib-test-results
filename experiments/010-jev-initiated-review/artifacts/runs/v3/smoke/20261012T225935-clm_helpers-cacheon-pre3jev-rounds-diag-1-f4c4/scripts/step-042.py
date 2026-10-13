import json
c=json.load(open('/task/workspace/context.json'))
keep=('n1','n2','n3','n4','n5','n6')
c['entries']=[e for e in c['entries'] if e['id'] in keep]
c['entries'].append({'id':'n8','role':'note','body':'R9: r09 board.md:3 Thread B adds checkout-api (MEMORY_LEAK ongoing). r09 board.md:4 Thread C opened shipping-svc pod failures, cause unknown, ongoing; r09 shipping-svc.log:1 config validation failed db.pool_max=-4 build 5.26.1 (ties CHG-120 r02 changes.md:4 -> likely BAD_CONFIG_ROLLOUT). r09 notify cache miss storm lines 5-85 (Thread D continues). Next: advance to R10.'})
json.dump(c,open('/task/workspace/context.json','w'))