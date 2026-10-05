import re,ctx
for i,l in enumerate(open('/task/fixtures/round-04/logs/checkout-api.log'),1):
  if re.search('WARN|ERR|status=4|status=5|upstream',l):print(i,l.rstrip()[:140])
c=ctx.load()
notes=[e['body'] for e in c['entries'] if e['role']=='note']
notes.append('R4: board.md:3 Thread A mitigated (CHG-136 APPLIED changes.md:4 mitigation ledger-svc). board.md:4 Thread B checkout-api UPSTREAM_RATE_LIMIT ongoing (verify logs). board.md:5 Thread D DISK_PRESSURE search-api ongoing; search-api.log:12-62 disk WARN 92-98%. Follow-ups OPEN board.md:6-8 CUSTOMER_COMMS, POSTMORTEM_DRAFT, CAPACITY_REVIEW.')
ctx.reset(notes)