open('/task/workspace/notes.md','a').write('\nR3: board.md:3 CUSTOMER_COMMS CLOSED. changes.md:3 CHG-121 APPLIED retry budget idempotent GETs=1 (benign). No ERROR/WARN lines besides slow query/heap.\n')
import glob
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
    c=sum('heap usage' in l for l in open(f)); print(f.split('/')[-1],c)
