import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6','n7')]
c['entries'].append({'id':'n8a','role':'note','body':'R8 advanced; scan output in /task/workspace/spill/s22.obs.txt'})
json.dump(c,open('/task/workspace/context.json','w'))
t=open('/task/workspace/spill/s22.obs.txt').read()
print(t[:3000])