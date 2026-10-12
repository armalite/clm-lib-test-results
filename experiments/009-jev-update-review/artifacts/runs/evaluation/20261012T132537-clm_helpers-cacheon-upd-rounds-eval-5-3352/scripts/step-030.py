import re
for s in ['auth-svc','ledger-svc','checkout-api','search-api','shipping-svc']:
  L=open(f'/task/fixtures/round-12/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:110]) for i,l in enumerate(L) if re.search(r'cert|pool|config|disk|ERROR|resolv|recover|healthy',l,re.I)]
  print(s,len(h),h[:3])
print(open('/task/fixtures/round-12/board.md').read())