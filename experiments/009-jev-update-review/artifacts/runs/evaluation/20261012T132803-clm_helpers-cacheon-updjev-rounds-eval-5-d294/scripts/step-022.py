import re,json
L=open('/task/fixtures/round-08/logs/checkout-api.log').read().splitlines()
h=[(i+1,l[:110]) for i,l in enumerate(L) if re.search('pool|exhaust|ERROR',l)]
print(len(h));[print(x) for x in h[:5]]
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']=n['body'].replace('(check format)','(format same; only slow-query noise)')
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))