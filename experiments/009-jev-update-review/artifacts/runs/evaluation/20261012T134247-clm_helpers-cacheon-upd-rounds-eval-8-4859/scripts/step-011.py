import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R4 logs: auth heap high 6,14,16,22,31,49,53,54; inventory db pool exhausted 19,25,29,36,37,57,80; pricing heap high 1,5,6,9,11,18,32,43,50,59,70. No restarts/cert errors yet. Next: advance to R5.'
json.dump(c,open('/task/workspace/context.json','w'))