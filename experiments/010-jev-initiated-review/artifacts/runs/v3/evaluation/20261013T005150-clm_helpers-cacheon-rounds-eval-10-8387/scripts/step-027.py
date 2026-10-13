import json
n=open('notes.md').read()+"R9 board: C opened shipping-svc ongoing cause unknown (round-09/board.md:3); OPEN RUNBOOK_UPDATE (:4), CUSTOMER_COMMS (:5). shipping-svc config validation failed round-09/logs/shipping-svc.log:15-69 -> BAD_CONFIG_ROLLOUT from CHG-113 (round-01/changes.md:3). Next: advance to R10.\n"
open('notes.md','w').write(n)
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('context.json','w'))
print('ok')