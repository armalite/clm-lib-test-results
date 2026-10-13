import json
c=json.load(open('/task/workspace/context.json'))
n1=[e for e in c['entries'] if e['id']=='n1'][0]
b=n1['body']
i=b.find(' Next: grep pricing-svc.log r8 rest')
if i>0:b=b[:i]
b+=" r8 pricing-svc config validation failed cache.ttl_s=-1 lines 5,17,28,38,57,60,61,68,83. Next: advance round 9."
n1['body']=b
c['entries']=[n1]
json.dump(c,open('/task/workspace/context.json','w'))
print(len(b))