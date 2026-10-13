import json
n='R1: board empty; round-01/changes.md:3 CHG-108 APPLIED TLS session ticket rotation. Slow-query WARNs = noise everywhere.\nR2: board empty. round-02/changes.md:4 CHG-120 APPLIED search-api 8.48.0 sets http.max_inflight=-1 (possible BAD_CONFIG later); :5 CHG-121 shipping no cfg. ledger-svc DNS SERVFAIL host=geo.internal round-02/logs/ledger-svc.log:3-81 (lines 3,22,...,81) -> DNS_RESOLUTION candidate. search-api no errors yet.'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]}
json.dump(c,open('/task/workspace/context.json','w'))