print(open('/task/fixtures/round-11/board.md').read())
import glob
for p in sorted(glob.glob('/task/fixtures/round-11/logs/*.log')):
  L=open(p).read().splitlines();e=[i for i,l in enumerate(L,1) if 'ERROR' in l and 'slow' not in l]
  m=set(L[i-1].split('"msg":"')[1].split('"')[0] if '"msg":"' in L[i-1] else L[i-1][:60] for i in e)
  print(p.split('/')[-1],e[:12],m)
open('/task/workspace/notes.md','a').write('\nR10 refs: inventory cfg errors 13-50; ledger dns 2-81; pricing dns 1-54\n')