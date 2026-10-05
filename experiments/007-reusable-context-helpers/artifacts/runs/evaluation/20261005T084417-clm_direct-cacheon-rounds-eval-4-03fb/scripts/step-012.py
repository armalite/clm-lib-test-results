import json
n=json.load(open('/task/workspace/context.json'))['entries'][:3]
n.append({'id':'n4','role':'note','body':'R4: board.md:3 Thread B MEMORY_LEAK auth-svc ongoing (board claim; logs show no memory evidence). board.md:4 follow-up OPEN VENDOR_TICKET. auth-svc.log ERROR upstream 429 tax-provider 12,16,17,34,36,41 (UPSTREAM_RATE_LIMIT?); shipping-svc.log same 5,21,28,29,33,36. auth miss storm 1,2,18,23. pool WARN inventory 3,19,21; notify 11,31,41. Next: advance R5.'})
json.dump({'format':'clm-context/v1','entries':n},open('/task/workspace/context.json','w'))