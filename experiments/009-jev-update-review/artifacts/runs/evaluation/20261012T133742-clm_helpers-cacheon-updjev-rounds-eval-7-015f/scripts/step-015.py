import json
d=json.load(open('/task/workspace/context.json'))
d['entries']=[e for e in d['entries'] if e['id']=='n1']
d['entries'][0]['body']+=' r5 board empty; checkout disk 91-97 lines 1,7,56; search 429 18,25,77; shipping 429 26,38,71. Round 5 done; next: advance.'
json.dump(d,open('/task/workspace/context.json','w'))
print('ok')