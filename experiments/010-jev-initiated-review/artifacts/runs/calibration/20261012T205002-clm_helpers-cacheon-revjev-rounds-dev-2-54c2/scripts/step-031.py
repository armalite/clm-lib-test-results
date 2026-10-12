import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
c['entries'].append({'id':'n10','role':'note','body':'R10: board.md:3 Thread D closed false alarm (not incident); :4 CLOSED DATA_BACKFILL. changes CHG-175 noise. search-api config errs round-10/logs/search-api.log:1-60 (1,4,7,8,20,30,50,54,60; mix 429/config). CERT errs round-10/logs/auth-svc.log:10,17 shipping-svc.log:3,60. No errs checkout/inventory. Open followups: ALERT_TUNING, RUNBOOK_UPDATE. Next: advance.'})
json.dump(c,open('/task/workspace/context.json','w'))