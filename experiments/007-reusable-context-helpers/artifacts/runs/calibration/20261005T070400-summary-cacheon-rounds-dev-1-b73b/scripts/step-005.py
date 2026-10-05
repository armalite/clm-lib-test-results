open('/task/workspace/notes.md','a').write('''\nR2: board.md:3-5 follow-ups OPEN ALERT_TUNING, RUNBOOK_UPDATE, VENDOR_TICKET. changes.md:4 CHG-120 APPLIED notify-worker http.max_inflight=0 (possible BAD_CONFIG); changes.md:5 CHG-121 payments no config. auth-svc db pool exhausted WARNs at lines 1,3,15,22,23,25 + 3 more (9 total); no board thread yet. Other services: only noise.\n''')
b='/task/fixtures/round-02/logs/auth-svc.log'
for i,l in enumerate(open(b).read().splitlines(),1):
  if 'slow query' in l or ' INFO ' in l: continue
  if i>25: print(i,l[:150])
b='/task/fixtures/round-02/logs/notify-worker.log'
for i,l in enumerate(open(b).read().splitlines(),1):
  if 'slow query' not in l: print(i,l[:150])
