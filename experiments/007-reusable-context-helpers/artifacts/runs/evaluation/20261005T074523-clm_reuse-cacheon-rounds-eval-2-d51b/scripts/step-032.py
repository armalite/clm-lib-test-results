import ctx,json
d=json.load(open('context.json'))
n=[e for e in d['entries'] if e['id']=='notes'][0]['body']
n=n.replace(' Next: advance.','')+'\nR11: board.md:3 Thread B mitigated. DNS errors dwindle ledger-svc.log:2-40, pricing-svc.log:8-30. config fail inventory-svc.log:1-73. Next: advance.'
ctx.replace_all(n)
print('ok')