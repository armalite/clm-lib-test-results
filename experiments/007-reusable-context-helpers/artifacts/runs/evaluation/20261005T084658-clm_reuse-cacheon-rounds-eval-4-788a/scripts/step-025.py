import ctx,json
n=json.load(open('/task/workspace/context.json'))['entries'][0]['body']
ctx.keep_notes(n+' R8: board round-08/board.md:3 Thread A resolved; board.md:4 Thread B mitigated; board.md:5 Thread C search-api ongoing cause unknown (likely BAD_CONFIG_ROLLOUT from CHG-113 ttl=-1: search-api.log:24,34,36,41 config validation failed); board.md:6 CAPACITY_REVIEW OPEN. 429 reduced auth-svc.log:29,40 shipping-svc.log:41,42. Open followups: VENDOR_TICKET, CAPACITY_REVIEW.')
print('ok')