import json
p='/task/workspace/context.json'
c=json.load(open(p))
n=c['entries'][0]['body']+"\nR7 disk refs: round-07/logs/notify-worker.log:2-56, round-07/logs/shipping-svc.log:18-80.\nR8: board round-08/board.md:3 Thread A resolved; :4 Thread B mitigated; :5 Thread C search-api ongoing cause unknown; :6 VENDOR_TICKET CLOSED. changes.md:3 CHG-159 retry budget. search-api config validation failed http.max_inflight=-1 build 8.48.0 round-08/logs/search-api.log:9,19,22,59,61,68,75 (BAD_CONFIG_ROLLOUT, cite round-02/changes.md:4). disk WARNs notify round-08/logs/notify-worker.log:17,58; shipping round-08/logs/shipping-svc.log:14,28. Open follow-ups so far: DATA_BACKFILL, RUNBOOK_UPDATE."
c['entries']=[{'id':'n1','role':'note','body':n}]
json.dump(c,open(p,'w'))
print('ok')