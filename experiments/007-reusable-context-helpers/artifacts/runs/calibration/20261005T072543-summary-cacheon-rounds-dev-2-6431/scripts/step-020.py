import collections
L=open('/task/fixtures/round-07/logs/search-api.log').read().splitlines()
c=collections.Counter()
for l in L:
    if '"ERROR"' in l or '"WARN"' in l: c[l.split('"msg":')[1][:40]]+=1
print(c)
open('/task/workspace/notes.md','a').write('R7: board.md:3 ThreadB cause->CERT_EXPIRED. board.md:4 Thread D UPSTREAM_RATE_LIMIT search-api ongoing (429 tax-provider). search lines 4,5,20,22,25,47,64,66. auth 1,16,24,26,32,36,38,49,53,64. shipping 10,11,23,26,35,39,43,45,46,49,59,66.\n');print('ok')