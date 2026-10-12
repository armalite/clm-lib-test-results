L=open('/task/fixtures/round-08/logs/checkout-api.log').readlines()
print(len(L))
for i,l in enumerate(L[:6],1):print(i,l.strip()[:200])
import re
for i,l in enumerate(L,1):
  if re.search('(?i)pool|err|exhaust|fail',l):print(i,l.strip()[:160])