import ctx
n=[e for e in ctx.load()['entries'] if e['id']=='notes'][0]['body']
n+=" R10: board.md:3 CUSTOMER_COMMS CLOSED; CHG-173 PROPOSED noise. auth cfg errs auth-svc.log:13-60; cert search-api.log:20-37, shipping-svc.log:58-61. Next: advance to R11."
ctx.prune(keep=())
ctx.setnote('notes',n)
print('ok')