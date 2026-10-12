import json
t=open('/task/workspace/spill/s13.obs.txt').read()
lines=t.splitlines()
print('\n'.join(l[:120] for l in lines if 'board' in l or 'changes' in l or 'ERROR' in l or 'error' in l)[:2500])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
c['entries'].append({'id':'n4','role':'note','body':'R4 raw output in /task/workspace/spill/s13.obs.txt (board/changes/non-info logs). Analyse from that file.'})
json.dump(c,open('/task/workspace/context.json','w'))