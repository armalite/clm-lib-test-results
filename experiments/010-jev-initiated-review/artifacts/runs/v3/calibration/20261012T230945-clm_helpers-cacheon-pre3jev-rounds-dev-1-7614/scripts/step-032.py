import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in ('n1','n2','n3','n4')]
c['entries'].append({'id':'n5','role':'note','body':'Round 8 released; findings from spill/s30.obs.txt to be noted next step.'})
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/workspace/spill/s30.obs.txt').read()[:2700])