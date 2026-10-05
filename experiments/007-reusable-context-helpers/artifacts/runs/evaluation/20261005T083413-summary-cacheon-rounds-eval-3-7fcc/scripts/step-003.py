b='/task/fixtures/round-01/'
open('/task/workspace/notes.md','a').write('R1 changes: CHG-113 APPLIED search-api http.max_inflight=-1 (round-01/changes.md:4); CHG-109 PROPOSED; CHG-114 APPLIED checkout no cfg.\n')
print(open(b+'board.md').read()[:1200])
for i,l in enumerate(open(b+'logs/search-api.log'),1):
  if 'slow query' not in l and 'INFO' not in l: print(i,l[:140].strip())
