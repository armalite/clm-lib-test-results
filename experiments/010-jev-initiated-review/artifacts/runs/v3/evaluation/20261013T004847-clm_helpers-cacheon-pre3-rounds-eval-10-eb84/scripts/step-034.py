import re
print(open('/task/fixtures/round-09/board.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=open(f'/task/fixtures/round-09/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|429|SERVFAIL|FATAL|OOM',l)]
  print(s,len(h),h[:3],h[-1:] if h else '', L[h[0]-1][:150] if h else '')