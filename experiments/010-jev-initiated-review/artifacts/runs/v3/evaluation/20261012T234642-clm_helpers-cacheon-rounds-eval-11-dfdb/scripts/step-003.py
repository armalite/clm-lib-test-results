import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; logs only routine slow-query WARNs (all 5 svcs: shipping-svc, checkout-api, pricing-svc, inventory-svc, search-api). Noise. changes: round-01/changes.md:4 CHG-113 APPLIED checkout-api build 4.33.8 sets feature.batch_size=0 (suspicious BAD_CONFIG); line5 CHG-114 inventory-svc no config; CHG-111 PROPOSED only. R1 done -> advance next.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-01/changes.md').read().splitlines()[3])