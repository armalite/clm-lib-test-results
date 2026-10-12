import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R2 board empty. pricing-svc.log heap usage high WARNs lines 6,7,10,22,36,55,62,66,83 rss_mb 2216-3660, gc_pause rising to 1302 (suspect MEMORY_LEAK, no restarts yet).'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')