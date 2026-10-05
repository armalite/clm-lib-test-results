import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; changes.md:3 CHG-108 PROPOSED (HPA search, not applied). Logs only WARN slow query noise in all services (notify-worker, checkout-api, auth-svc, payments-svc, search-api). No incidents yet. Next: advance.'}]}
json.dump(c,open('/task/workspace/context.json','w'))