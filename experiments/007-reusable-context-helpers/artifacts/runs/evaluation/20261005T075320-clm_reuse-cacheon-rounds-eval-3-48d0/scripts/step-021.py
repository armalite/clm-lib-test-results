import ctx,json
ctx.keep_only(['n1','n2','n3','n4','n4b','n5','n6'])
d=json.load(open('context.json'))
d['entries'].append({'id':'n7','role':'note','body':'R7: board.md:3 A resolved; :4 Thread C search-api failures ongoing cause unknown; :5 D closed false alarm; :6 OPEN VENDOR_TICKET. search-api.log:17,20,23,28,30,39,50,52,58 ERROR config validation http.max_inflight=-1 (BAD_CONFIG_ROLLOUT, CHG-113 r1 changes.md:4). checkout heap WARN continues :6-67 (MEMORY_LEAK, thread B). Next: advance R8.'})
json.dump(d,open('context.json','w'))
print('ok')