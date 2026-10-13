import sys,json;sys.path.insert(0,'/task/workspace')
import cm
n=json.load(open('/task/workspace/context.json'))['entries'][0]['body']
n=n.replace(' Next: advance to R6.','')
cm.setnotes(n+' R6: round-06/board.md:3 Thread A mitigated; board.md:4 OPEN RUNBOOK_UPDATE; round-06/changes.md:4 CHG-150 APPLIED mitigation ledger. DNS logs gone R6. shipping tls round-06/logs/shipping-svc.log:1-86 (wide; split), shipping disk :13-70, notify disk round-06/logs/notify-worker.log:12-78. Next: advance to R7.')
print('ok')