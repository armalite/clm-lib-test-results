import json
p='/task/workspace/context.json'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: quiet; only slow-query WARNs in all 5 services (auth-svc, checkout-api, notify-worker, payments-svc, search-api). board empty. changes: CHG-108 PROPOSED raise HPA search (not applied). Scan method: grep WARN|ERROR|fail|429|timeout, dedupe by pattern.'}]}
json.dump(c,open(p,'w'))
print('ok')