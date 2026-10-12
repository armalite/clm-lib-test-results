import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; changes: CHG-108 PROPOSED raise HPA max search tier (not applied). Logs (auth,checkout,notify,payments,search): only background slow query WARNs, no incident. Next: advance.'}]}
json.dump(c,open('/task/workspace/context.json','w'))