b='/task/fixtures/stage-2/logs/payments-api.log'
for i,l in enumerate(open(b),1):
  if 'pool exhausted' in l: print(i,l.strip()[:200]);break
open('/task/workspace/notes.txt','w').write('stage2: CHG-5266 APPLIED timeout 4000 (changes.log:1). pool exhausted 10/10 from payments-api.log:136; metrics db_pool_in_use 10. pool max 10 from release notes line17. leading: DB_POOL_EXHAUSTED\n')