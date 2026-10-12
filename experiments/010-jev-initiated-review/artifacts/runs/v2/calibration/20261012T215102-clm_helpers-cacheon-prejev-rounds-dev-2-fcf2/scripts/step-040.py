import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
b=n['body']
b=b.split('\nR9:')[0]
b+="\nR9: round-09/board.md:3 Thread C note pods still restarting, ongoing. changes.md:3 CHG-166 noise. search-api 429 tax-provider round-09/logs/search-api.log:1,5,11,20; config validation failed http.max_inflight round-09/logs/search-api.log:2,9,13,19. CERT still auth-svc.log:22,55; shipping-svc.log:28,56. No DNS. Next: advance to R10."
n['body']=b
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
print(len(b))