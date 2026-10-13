import json
s=open('/task/workspace/spill/s42.obs.txt').read()
print(s[:2500])
ctx=json.load(open('/task/workspace/context.json'))
n1=[e for e in ctx['entries'] if e['id']=='n1'][0]
n1['body']=n1['body'].replace(' Next: advance to R10.','')+'\nR10: raw grep output saved at /task/workspace/spill/s42.obs.txt (read it next step and summarise).'
ctx['entries']=[n1]
json.dump(ctx,open('/task/workspace/context.json','w'))