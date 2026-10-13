import json
e=json.load(open('/task/workspace/context.json'))['entries']
keep=[x for x in e if x['id'].startswith('n')]
keep.append({'id':'n8','role':'note','body':'Round8: board: Thread A resolved (round-08/board.md:3); Thread B mitigated (round-08/board.md:4); Thread C opened search-api failures cause unknown ongoing (round-08/board.md:5); Follow-up CLOSED VENDOR_TICKET (round-08/board.md:6). changes: CHG-159 APPLIED retry budget (round-08/changes.md:3). Log format now JSON. search-api ERROR config validation failed key=http.max_inflight round-08/logs/search-api.log:9,19,22,59,61,68,75 -> BAD_CONFIG_ROLLOUT from CHG-120 (round-02/changes.md:4). disk WARN notify-worker:17,58 shipping-svc:14,28. Open followups: DATA_BACKFILL, RUNBOOK_UPDATE. Next: advance to round 9.'})
json.dump({'format':'clm-context/v1','entries':keep},open('/task/workspace/context.json','w'))
print('ok')