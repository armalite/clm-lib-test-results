import json
d=json.load(open('/task/workspace/context.json'))
d['entries']=[e for e in d['entries'] if e['id']=='n1']
d['entries'][0]['body']+=' r6 logs: no 429s at all (shipping/search quiet); checkout disk used_pct 91-98 lines 1,31,74. Round 6 done; next: advance.'
json.dump(d,open('/task/workspace/context.json','w'))
print('ok')