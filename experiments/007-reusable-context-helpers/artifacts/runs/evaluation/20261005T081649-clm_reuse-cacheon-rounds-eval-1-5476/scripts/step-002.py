import ctx
ctx.prune(keep=())
ctx.setnote('notes','R1: board empty. Logs: slow query WARNs everywhere (noise). payments-svc consumer lag topic=stock-updates round-01/logs/payments-svc.log:7,9,10,31,34,43 (fluctuating, maybe noise). ctx.py has load/save/setnote(id,body)/prune(keep).')
print(open('/task/fixtures/round-01/changes.md').read()[:1500])