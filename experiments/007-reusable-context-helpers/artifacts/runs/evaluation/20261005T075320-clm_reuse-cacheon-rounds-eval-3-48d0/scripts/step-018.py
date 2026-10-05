import ctx,json
ctx.keep_only(['n1','n2','n3','n4','n4b','n5'])
d=json.load(open('context.json'))
d['entries'].append({'id':'n6','role':'note','body':'R6: board.md:3 CLOSED CUSTOMER_COMMS. changes.md:3 CHG-147 APPLIED TLS ticket rotation. checkout-api.log:17,24,35,42,53,59,61,66 heap WARN (no 429). search-api.log:6,22,28,30,38,39,46,74 disk 91-97%. Next: advance R7.'})
json.dump(d,open('context.json','w'))
print('ok')