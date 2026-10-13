import re
print(open('/task/fixtures/round-10/board.md').read())
for i,l in enumerate(open('/task/fixtures/round-10/logs/shipping-svc.log'),1):
  if re.search('config|backoff|6.58',l): print(i,l.strip()[:160])