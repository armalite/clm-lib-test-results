open('/task/workspace/notes.md','a').write('\nR10: board C note still restarting round-10/board.md:3; CHG-170 PROPOSED. B dns errors continue ledger/pricing.\n')
import glob
for p in sorted(glob.glob('/task/fixtures/round-10/logs/*.log')):
  L=open(p).read().splitlines();e=[i for i,l in enumerate(L,1) if 'ERROR' in l and 'slow' not in l]
  m=set(L[i-1].split('"msg":"')[1].split('"')[0] for i in e) if e else set()
  print(p.split('/')[-1],e[:12],m)