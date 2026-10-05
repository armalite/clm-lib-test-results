import json
n=open('/task/workspace/notes.txt').read()+'\nR7: board A resolved (round-07/board.md:3); C search-api failures cause unknown ongoing (:4); D closed false alarm (:5); FU OPEN VENDOR_TICKET (:6). search-api ERROR config validation http.max_inflight=-1 build 4.16.4 round-07/logs/search-api.log:17-58 (=> C is BAD_CONFIG_ROLLOUT from CHG-113). checkout heap WARNs round-07/logs/checkout-api.log:6-67; others clean. Next: advance to r8.'
open('/task/workspace/notes.txt','w').write(n)
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))
print('ok')