import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; changes.md:3 CHG-108 PROPOSED (not applied) HPA search. Logs only background slow-query WARNs (noise) in all 5 services (auth-svc,checkout-api,notify-worker,payments-svc,search-api). No incidents yet.'}]}
json.dump(c,open('/task/workspace/context.json','w'))