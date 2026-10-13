import json
s=open('/task/workspace/spill/s32.obs.txt').read()
print(s[:3200])
ctx=json.load(open('/task/workspace/context.json'))
n1=[e for e in ctx['entries'] if e['id']=='n1'][0]
n1['body']=n1['body'].replace(' Next: advance to R8.','')+'\nR8: released; raw obs in /task/workspace/spill/s32.obs.txt (summarize next step).'
ctx['entries']=[n1]
json.dump(ctx,open('/task/workspace/context.json','w'))