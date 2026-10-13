import json
print(open('/task/fixtures/round-09/board.md').read())
for i,l in enumerate(open('/task/fixtures/round-09/logs/search-api.log'),1):
    if 'ERROR' in l or 'max_inflight' in l: print(i,l.strip()[:120])
c=json.load(open('/task/workspace/context.json'))
E={e['id']:e for e in c['entries']}
E['n8']['body']=E['n8']['body'].replace(' Next: advance to round 9.','')
E['n9']={'id':'n9','role':'note','body':'Round9 released; see round-09/board.md (read at step 36).'}
c['entries']=[E[k] for k in ['n1','n2','n3','n4','n5','n6','n7','n8','n9']]
json.dump(c,open('/task/workspace/context.json','w'))