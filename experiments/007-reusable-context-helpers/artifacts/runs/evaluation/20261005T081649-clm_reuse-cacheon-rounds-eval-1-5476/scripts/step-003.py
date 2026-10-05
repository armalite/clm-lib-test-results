import ctx
ctx.prune(keep=())
ctx.setnote('notes','R1: board empty. slow query WARNs noise. payments-svc consumer lag stock-updates r01 payments-svc.log:7,9,10,31,34,43 (maybe noise). changes r01: CHG-113 APPLIED auth-svc build 4.51.3 sets cache.ttl_s=-1 (round-01/changes.md:4) suspect BAD_CONFIG; CHG-112 TLS ticket hourly; CHG-114 shipping no cfg. ctx.py load/save/setnote/prune(keep).')
import re
for i,l in enumerate(open('/task/fixtures/round-01/logs/auth-svc.log'),1):
  if re.search('ERROR|ttl|cache',l,re.I): print(i,l.strip()[:160])