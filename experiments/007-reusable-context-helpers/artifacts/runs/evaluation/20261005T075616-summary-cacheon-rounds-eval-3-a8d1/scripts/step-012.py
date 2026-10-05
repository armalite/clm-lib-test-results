import re,glob
open('/task/workspace/notes.md','a').write('\nR4: board A mitigated (board.md:3, CHG-136 changes.md:4 mitigation ledger). B opened checkout-api suspected UPSTREAM_RATE_LIMIT (board:4) but logs show heap usage high lines 18-90 -> likely MEMORY_LEAK. D opened DISK_PRESSURE search-api (board:5), logs search-api 12-62 disk high. FU open: CUSTOMER_COMMS, POSTMORTEM_DRAFT, CAPACITY_REVIEW (board 6-8).\n')
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'429|restart|OOM|cert|tls|ERROR',l,re.I): print(f.split('/')[-1],i,l.strip()[:130])