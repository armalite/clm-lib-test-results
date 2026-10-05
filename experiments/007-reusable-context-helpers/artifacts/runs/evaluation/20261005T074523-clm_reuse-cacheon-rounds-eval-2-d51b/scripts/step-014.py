import ctx,json
d=json.load(open('context.json'))
n=[e for e in d['entries'] if e['id']=='notes'][0]['body']
n=n.replace(' Next: advance.','')+'\nR05: board empty. DNS SERVFAIL rates.internal continues ledger-svc.log:14-49. Next: advance.'
ctx.replace_all(n)
print('ok')