import json
print(open('/task/fixtures/round-09/board.md').read())
print(open('/task/workspace/spill/s38.obs.txt').read()[:2500])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in ('n1','n2','n3','n4','n5','n6')]
c['entries'].append({'id':'n8','role':'note','body':'R9 released; board/log scan output in spill/s38.obs.txt (re-read if needed).'})
json.dump(c,open('/task/workspace/context.json','w'))