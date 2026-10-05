import ctx,json
ctx.keep_only(['n1','n2','n3','n4','n4b','n5','n6','n7','n8'])
d=json.load(open('context.json'))
d['entries'].append({'id':'n9','role':'note','body':'R9: board.md:3 B services +payments-svc; :4 B mitigated. changes.md:3 CHG-164 APPLIED log sampling (irrelevant). checkout-api.log:27,56 heap; payments-svc.log:45,55 heap; search-api.log:5,11,14,22,33,46,58 cfg errors (C ongoing). Next: advance R10.'})
json.dump(d,open('context.json','w'))
print('ok')