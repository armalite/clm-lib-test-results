open('/task/workspace/notes.md','a').write('S2: changes.log:1 CHG-5117 APPLIED timeout 3500 09:35. New errors db pool exhausted 14/14 first quotes-api.log:136 (09:37:50). pool 14 from release-notes:15. Hypothesis DB_POOL_EXHAUSTED.\n')
b='/task/fixtures/stage-2/'
L=open(b+'metrics/quotes-api.csv').readlines()
print(L[0].strip());[print(i,L[i-1].strip()) for i in (30,40,50,61)]