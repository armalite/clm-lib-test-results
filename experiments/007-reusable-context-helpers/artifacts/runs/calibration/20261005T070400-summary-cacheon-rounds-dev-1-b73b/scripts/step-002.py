b='/task/fixtures/round-01/'
for i,l in enumerate(open(b+'changes.md').read().splitlines(),1): print(i,l[:200])
open('/task/workspace/notes.md','a').write('R1: board empty; only slow query WARNs in all logs (noise).\n')