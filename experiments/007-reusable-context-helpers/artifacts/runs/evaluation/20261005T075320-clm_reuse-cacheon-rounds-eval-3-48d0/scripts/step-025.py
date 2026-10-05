import ctx
ctx.keep_only(['n1','n2','n3','n4','n4b','n5','n6','n7'])
import json
d=json.load(open('context.json'))
d['entries'].append({'id':'n8','role':'note','body':'R8: board.md:3 B cause MEMORY_LEAK; :4 C ongoing; :5 CLOSED VENDOR_TICKET. changes.md:3 CHG-160 PROPOSED. checkout-api.log:9,15,46,48,56,69 heap; payments-svc.log:13,24,26,31,34,41,54,62 heap; search-api.log:2-76 cfg errors; ledger-svc.log:22 429?'})
json.dump(d,open('context.json','w'))
L=open('/task/fixtures/round-08/logs/ledger-svc.log').read().splitlines()
print(L[21][:200])
P=open('/task/fixtures/round-08/logs/payments-svc.log').read().splitlines()
print(P[12][:200])