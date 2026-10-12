import h,json
b=json.load(open('context.json'))['entries'][0]['body']
b+='\nR10: board.md:3 Thread D false alarm (drop UPSTREAM_RATE_LIMIT); :4 CLOSED DATA_BACKFILL. CHG-175 noise. search-api config fail continues search-api.log:1,4,54,60. CERT auth-svc.log:10,17 shipping-svc.log:3,60.'
h.setctx([{'id':'n1','role':'note','body':b}])
print('ok')