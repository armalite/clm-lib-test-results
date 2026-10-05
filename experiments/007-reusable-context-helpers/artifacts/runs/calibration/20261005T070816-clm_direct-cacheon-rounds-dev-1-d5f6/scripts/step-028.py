import json
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
c['entries'].append({'id':'n9','role':'note','body':'R9: Thread B MITIGATED (round-09/board.md:3); 429 round-09/logs/checkout-api.log:34, payments-svc.log:34. Thread C ongoing (round-09/board.md:4); notify-worker.log:3 max_inflight=0. CHG-164 irrelevant. Next: advance R10.'})
json.dump(c,open(p,'w'))