import ctx,json
ctx.keep_only(['n1','n2','n3','n4','n4b'])
d=json.load(open('context.json'))
d['entries'].append({'id':'n5','role':'note','body':'R5: board.md:3 OPEN DATA_BACKFILL. checkout-api.log:6,24,25,31,32,35,51,77 heap WARN rss up to 3773 (no 429). search-api.log:14,31,35,46,61,70,76 disk 91-98%. no changes.md. Next: advance R6.'})
json.dump(d,open('context.json','w'))
print('ok')