import json
s=open('/task/workspace/spill/s25.obs.txt').read()
print(s[:2800])
c=json.load(open('/task/workspace/context.json'))
keep=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6')]
keep.append({'id':'n7raw','role':'note','body':'Round7 raw scan saved in /task/workspace/spill/s25.obs.txt (summarize next step).'})
c['entries']=keep
json.dump(c,open('/task/workspace/context.json','w'))