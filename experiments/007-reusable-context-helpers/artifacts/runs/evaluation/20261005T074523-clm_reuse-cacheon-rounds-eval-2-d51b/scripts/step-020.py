import ctx,json
d=json.load(open('context.json'))
n=[e for e in d['entries'] if e['id']=='notes'][0]['body']
n=n.replace(' Next: advance.','')+'\nR07: board.md:3 Thread B +pricing-svc; board.md:4 Thread D CERT_EXPIRED inventory-svc ongoing (logs inventory-svc.log:7-68 partner-gw cert expired, real). changes.md:3 CHG-151 PROPOSED (noise). DNS continues ledger-svc.log:4-73, pricing-svc.log:6-61. Next: advance.'
ctx.replace_all(n)
print('ok')