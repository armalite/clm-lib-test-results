import ctx,json
d=json.load(open('context.json'))
n=[e for e in d['entries'] if e['id']=='notes'][0]['body']
n=n.replace(' Next: advance.','')+'\nR08: board empty. CHG-156 noise. cert continues inventory-svc.log:6-78; DNS ledger-svc.log:2-64, pricing-svc.log:4-51. Next: advance.'
ctx.replace_all(n)
print('ok')