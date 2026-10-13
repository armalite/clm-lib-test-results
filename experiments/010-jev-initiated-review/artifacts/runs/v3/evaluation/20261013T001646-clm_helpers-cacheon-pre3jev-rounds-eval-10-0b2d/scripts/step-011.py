import json
b='''R1: only background slow-query WARNs (noise). changes r1: CHG-113 APPLIED build 6.58.8 shipping-svc sets retry.backoff_ms=0 (round-01/changes.md:3); CHG-114 APPLIED 6.58.8 search-api no config (line 4).
R2: board follow-ups OPEN DATA_BACKFILL, POSTMORTEM_DRAFT (round-02/board.md:3-4). auth-svc dns SERVFAIL host=geo.internal round-02/logs/auth-svc.log:4-72.
R3: board Thread A DNS_RESOLUTION confirmed auth-svc + checkout-api, ongoing (round-03/board.md:3). Thread B search-api suspected DB_POOL_EXHAUSTED ongoing (board.md:4) BUT logs show search-api ERROR 429 upstream=fx-rates (round-03/logs/search-api.log:16,24,30,33; 10 errors) -> likely UPSTREAM_RATE_LIMIT. checkout dns errors round-03/logs/checkout-api.log:14,18,22,25; auth round-03/logs/auth-svc.log:2,15,20,25. changes r3 CHG-123 dashboards only (noise). inventory, shipping no errors r3.
Next: advance to round 4.'''
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':b}]}
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')