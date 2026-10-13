import json
n=json.load(open('/task/workspace/context.json'))['entries'][0]['body'].replace(' Next: advance to round 8.','')
n+='\nRound8: board round-08/board.md:3 Thread A resolved; :4 DATA_BACKFILL OPEN. CHG-157 noise. DNS SERVFAIL kms.internal round-08/logs/inventory-svc.log:6-72. Others no errors. Open: POSTMORTEM_DRAFT, CAPACITY_REVIEW, DATA_BACKFILL. Next: advance to round 9.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))