import json
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6','n7')]
c['entries'].append({'id':'n8','role':'note','body':'R8 released; raw output in /task/workspace/spill/s29.obs.txt (read board/changes lines first).'})
json.dump(c,open(p,'w'))
t=open('/task/workspace/spill/s29.obs.txt').read()
print(t[:2500])