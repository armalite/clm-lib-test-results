import json,re
c=json.load(open('/task/workspace/context.json'))
b=c['entries'][0]['body'].replace(' Next: advance to R5.','')
b+=' R5 board: Thread B adds ledger-svc round-05/board.md:3; Thread D DNS closed false alarm board.md:4 (but logs showed SERVFAIL - recheck); CAPACITY_REVIEW open board.md:5. R5 changes.md:3 CHG-136 PROPOSED (different text than R4 CHG-136 APPLIED; recheck).'
for s in ['pricing-svc','inventory-svc','ledger-svc','notify-worker','search-api']:
  L=open(f'/task/fixtures/round-05/logs/{s}.log').read().splitlines()
  h=[f'{i+1}' for i,l in enumerate(L) if re.search(r'SERVFAIL|cert|disk|pool|miss|ERROR',l,re.I)]
  print(s,len(h),h[:8],L[int(h[0])-1][:150] if h else '')
c['entries']=[{'id':'notes','role':'note','body':b}]
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-04/changes.md').read())