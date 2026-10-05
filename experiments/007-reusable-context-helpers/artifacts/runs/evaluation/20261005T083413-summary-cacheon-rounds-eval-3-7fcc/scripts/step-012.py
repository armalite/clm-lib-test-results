open('/task/workspace/notes.md','a').write('\nR4: board A mitigated (round-04/board.md:3); B checkout UPSTREAM_RATE_LIMIT ongoing (b:4); D search DISK_PRESSURE ongoing (b:5); FU open CUSTOMER_COMMS, POSTMORTEM_DRAFT, CAPACITY_REVIEW (b:6-8). CHG-136 APPLIED A mitigation ledger (round-04/changes.md:4). checkout heap warns 18-20; search disk 12,13,21.\n')
for s in ['checkout-api','search-api']:
  for i,l in enumerate(open(f'/task/fixtures/round-04/logs/{s}.log'),1):
    if ' INFO ' not in l and 'slow query' not in l: print(s,i,l.strip()[11:])