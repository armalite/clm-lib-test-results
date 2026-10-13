import json
b='/task/fixtures/round-01/'
ch=open(b+'changes.md').read()
print(ch[:1500])
c=json.load(open('context.json'))
E=[e for e in c['entries'] if e['id'] not in ('s1.act','s1.obs','s2.act','s2.obs')]
E.append({'id':'n1','role':'note','body':'R1: board empty. logs (notify-worker,checkout-api,auth-svc,payments-svc,search-api) only WARN slow query ms~200-450 baseline noise, no errors. changes.md: '+ch[:600]})
c['entries']=E
json.dump(c,open('context.json','w'))