import re
for i,l in enumerate(open('/task/fixtures/round-02/logs/shipping-svc.log'),1):
  if 'slow query' not in l:print(i,l.strip()[:130])