import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; changes.md:3 CHG-108 APPLIED TLS session ticket rotation hourly. Logs (inventory,ledger,notify-worker,search-api,shipping) only background slow-query WARNs = noise. Next: advance.'}]}
json.dump(c,open('/task/workspace/context.json','w'))