import json
c=json.load(open('/task/workspace/context.json'))
body='''CHG-113 APPLIED checkout-api db.pool_max=-4 (round-01/changes.md:4). Thread A DISK_PRESSURE search-api+shipping-svc (round-02/board.md:3), mitigated via CHG-136 (round-04/changes.md:4, round-04/board.md:3), resolved (round-07/board.md:3). Thread B auth-svc opened MEMORY_LEAK (round-03/board.md:3) revised CERT_EXPIRED (round-07/board.md:4), ongoing; logs certificate_expired peer=bank-api through R9 (round-09/logs/auth-svc.log:6,18,22,25,53). Thread D DB_POOL checkout-api (round-06/board.md:3) closed false alarm (round-08/board.md:3); watch CHG-113. OPEN follow-ups: CUSTOMER_COMMS (round-02/board.md:4), DATA_BACKFILL, VENDOR_TICKET (round-04/board.md:4,5), CAPACITY_REVIEW (round-05/board.md:3), ALERT_TUNING (round-07/board.md:5). R9 logs checked; R9 board not yet reviewed in notes. Next: advance to R10.'''
c['entries']=[{'id':'sum1','role':'summary','body':body}]
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-09/board.md').read()[:1500])
try: print(open('/task/fixtures/round-09/changes.md').read()[:800])
except Exception as e: print(e)