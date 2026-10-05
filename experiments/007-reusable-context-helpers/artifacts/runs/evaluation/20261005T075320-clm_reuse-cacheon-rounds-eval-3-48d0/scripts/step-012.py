import ctx,json
ctx.keep_only(['n1','n2','n3','n4'])
d=json.load(open('context.json'))
d['entries'].append({'id':'n4b','role':'note','body':'R4 checkout-api.log:18-20,35,41,42,88,90 heap WARN rss_mb up to 3821 gc pauses (no 429 seen) -> maybe MEMORY_LEAK not rate limit. Next: advance to R5.'})
json.dump(d,open('context.json','w'))
print('ok')