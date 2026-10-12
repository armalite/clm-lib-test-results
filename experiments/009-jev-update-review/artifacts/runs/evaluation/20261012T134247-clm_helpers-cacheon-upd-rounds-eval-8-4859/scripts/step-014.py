import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R5 board empty. R5 logs: auth heap high 6,10,13,16,19,33,44,46,52,53,60,65; inventory db pool exhausted 6,17,37,47,54,64,67; pricing heap high 3,7,11,34,42,48,50. Next: advance to R6.'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')