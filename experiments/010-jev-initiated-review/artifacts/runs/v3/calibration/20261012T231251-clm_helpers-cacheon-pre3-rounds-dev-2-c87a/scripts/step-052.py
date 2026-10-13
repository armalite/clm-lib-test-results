import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
n['body']=n['body'].replace(' Next: advance to round 11.',' R11 released; board 2 lines (no board/change update per review). Spill at /task/workspace/spill/s50.obs.txt.')
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/workspace/spill/s50.obs.txt').read()[:2500])