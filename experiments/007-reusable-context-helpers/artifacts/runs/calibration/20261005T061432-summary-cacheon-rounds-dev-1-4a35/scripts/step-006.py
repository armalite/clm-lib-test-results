import re
for i,l in enumerate(open('/task/fixtures/round-02/logs/search-api.log'),1):
    if i>=39 and not re.search(r'gc cycle|slow query|request ok|heartbeat|health ok',l): print(i,l.rstrip())
open('/task/workspace/notes.md','a').write('\nR2: follow-ups OPEN ALERT_TUNING(b:3),RUNBOOK_UPDATE(b:4),VENDOR_TICKET(b:5). CHG-120 APPLIED notify-worker max_inflight=0 (changes.md:4). auth-svc db pool exhausted lines 1,3,15,22,23,25,44,65,69.\n')