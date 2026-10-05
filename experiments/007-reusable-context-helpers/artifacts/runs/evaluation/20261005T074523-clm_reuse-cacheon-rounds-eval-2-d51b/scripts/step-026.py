import ctx,json
d=json.load(open('context.json'))
n=[e for e in d['entries'] if e['id']=='notes'][0]['body']
n=n.replace(' Next: advance.','')+'\nR09: board.md:3 Thread B cause=DNS_RESOLUTION; board.md:4 Thread C inventory-svc ongoing cause unknown (logs inventory-svc.log:2-71 config validation failed retry.backoff_ms=0 -> BAD_CONFIG_ROLLOUT from CHG-120 r02 changes.md:3); board.md:5 Thread D FALSE ALARM (drop cert); board.md:6 POSTMORTEM_DRAFT OPEN. DNS ledger-svc.log:3-68, pricing-svc.log:3-62. auth/payments clean. Next: advance.'
ctx.replace_all(n)
print('ok')