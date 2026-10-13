import re
for s in ['notify-worker','shipping-svc']:
  L=[(i,l.strip()[:150]) for i,l in enumerate(open(f'/task/fixtures/round-07/logs/{s}.log'),1) if re.search('disk|volume',l,re.I)]
  print(s,L[0],L[-1])