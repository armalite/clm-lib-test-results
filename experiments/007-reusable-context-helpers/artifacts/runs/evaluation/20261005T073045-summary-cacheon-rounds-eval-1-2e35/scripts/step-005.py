open('/task/workspace/notes.md','a').write('\nR2: board Thread A QUEUE_BACKLOG payments-svc+ledger-svc ongoing (round-02/board.md:3). CHG-117 APPLIED TLS rotation. lag topic=stock-updates in ledger+payments.\n')
import os,glob
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  if 'ledger' in f or 'payments' in f: continue
  for i,l in enumerate(open(f),1):
    if 'INFO' in l or 'slow query' in l: continue
    print(os.path.basename(f),i,l.rstrip()[:140])