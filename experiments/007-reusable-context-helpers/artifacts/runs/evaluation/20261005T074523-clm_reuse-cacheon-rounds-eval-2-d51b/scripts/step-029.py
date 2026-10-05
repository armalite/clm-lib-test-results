import ctx,json
d=json.load(open('context.json'))
n=[e for e in d['entries'] if e['id']=='notes'][0]['body']
n=n.replace(' Next: advance.','')+'\nR10: board.md:3 Thread C still restarting. CHG-170 PROPOSED noise. config fail inventory-svc.log:13-50; DNS ledger-svc.log:2-81, pricing-svc.log:1-54. Next: advance.'
ctx.replace_all(n)
print('ok')