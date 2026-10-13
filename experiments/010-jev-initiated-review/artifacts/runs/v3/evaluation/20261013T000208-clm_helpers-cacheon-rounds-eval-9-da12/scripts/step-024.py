import sys,json;sys.path.insert(0,'/task/workspace')
import cm
n=json.load(open('/task/workspace/context.json'))['entries'][0]['body']
n=n.replace(' Next: advance to R8.','')
cm.setnotes(n+' R8: round-08/board.md:3 Thread A resolved; board.md:4 Thread B mitigated; board.md:5 Thread C search-api ongoing (cause unknown; logs show config validation failed http.max_inflight=-1 -> BAD_CONFIG_ROLLOUT via CHG-120) round-08/logs/search-api.log:9-22, :68-75; board.md:6 CLOSED VENDOR_TICKET. CHG-159 noise. disk shipping round-08/logs/shipping-svc.log:14-28 notify round-08/logs/notify-worker.log:17. Open now: DATA_BACKFILL, RUNBOOK_UPDATE. Next: advance to R9.')
print('ok')