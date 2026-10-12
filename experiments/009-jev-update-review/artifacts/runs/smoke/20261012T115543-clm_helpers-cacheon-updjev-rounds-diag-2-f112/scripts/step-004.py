for i,l in enumerate(open('/task/fixtures/round-01/logs/notify-worker.log'),1):
  if 'slow' not in l.lower(): print(i,l.strip()[:150])
