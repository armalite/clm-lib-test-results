import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
for x in c['entries']:
  if x['id']=='n10': x['body']+=' R10 board.md:3 Thread C opened checkout-api failures cause unknown ongoing (=BAD_CONFIG). changes.md:3 CHG-173 PROPOSED ignore. R10 done; next: advance.'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')