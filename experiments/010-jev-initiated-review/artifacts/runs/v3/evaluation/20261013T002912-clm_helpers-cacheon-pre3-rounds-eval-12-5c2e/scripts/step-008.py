import json
n1='R1: CHG-110 APPLIED retry budget GETs=1 (round-01/changes.md:3); CHG-113 APPLIED pricing-svc 3.22.4 cache.ttl_s=-1 (round-01/changes.md:4) possible BAD_CONFIG_ROLLOUT; CHG-114 APPLIED ledger-svc 3.22.4 (round-01/changes.md:5). R1 logs only slow-query noise.'
n2='R2: board: Follow-up OPEN CAPACITY_REVIEW (round-02/board.md:3). changes: CHG-115 APPLIED retry budget GETs=1 (round-02/changes.md:3). search-api ERROR tls handshake peer=sso.example.net certificate_expired lines 11,15,19,24,27,33,57 (round-02/logs/search-api.log) -> CERT_EXPIRED on search-api, not on board yet. Next: advance to round 3.'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1},{'id':'n2','role':'note','body':n2}]}
json.dump(c,open('/task/workspace/context.json','w'))