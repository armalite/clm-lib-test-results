import sys,json;sys.path.insert(0,'/task/workspace')
import cm
n=json.load(open('/task/workspace/context.json'))['entries'][0]['body']
n=n.replace(' Next: advance to R7.','')
cm.setnotes(n+' R7: round-07/board.md:3 Thread B cause revised DISK_PRESSURE; board.md:4 Thread D false alarm (drop); board.md:5 CLOSED POSTMORTEM_DRAFT. CHG-149 PROPOSED (noise). shipping disk round-07/logs/shipping-svc.log:18-80 (split), notify disk round-07/logs/notify-worker.log:2-56. Open now: DATA_BACKFILL, VENDOR_TICKET, RUNBOOK_UPDATE. Next: advance to R8.')
print('ok')