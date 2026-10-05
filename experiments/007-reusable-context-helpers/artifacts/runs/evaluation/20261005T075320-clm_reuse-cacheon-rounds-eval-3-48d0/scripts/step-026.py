import ctx,json
ctx.keep_only(['n1','n2','n3','n4','n4b','n5','n6','n7'])
d=json.load(open('context.json'))
d['entries'].append({'id':'n8','role':'note','body':'R8: board.md:3 B cause MEMORY_LEAK; :4 C ongoing; :5 CLOSED VENDOR_TICKET. changes.md:3 CHG-160 PROPOSED. checkout-api.log:9,15,46,48,56,69 heap; payments-svc.log:13,24,26,31,34,41,54,62 heap WARN rss~2159 (memory leak also payments?); search-api.log:2-76 cfg errors; ledger fine. Next: advance R9.'})
json.dump(d,open('context.json','w'))
print('ok')