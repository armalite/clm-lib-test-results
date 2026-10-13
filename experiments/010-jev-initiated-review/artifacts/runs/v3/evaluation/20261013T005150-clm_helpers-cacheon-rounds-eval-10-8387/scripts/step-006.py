import json
n=open('notes.md').read()+"R2: board OPEN DATA_BACKFILL (round-02/board.md:3), POSTMORTEM_DRAFT (:4). auth-svc DNS SERVFAIL host=geo.internal round-02/logs/auth-svc.log:4-15,37-72. No incident thread on board yet.\n"
open('notes.md','w').write(n)
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('context.json','w'))
print('ok')