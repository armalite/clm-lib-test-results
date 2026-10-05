import glob
for f in ['search-api','payments-svc']:
  try:
    for i,l in enumerate(open(f'/task/fixtures/round-08/logs/{f}.log'),1):
      if '"INFO"' not in l: print(f,i,l.strip()[:150])
  except Exception as e: print(e)