import json
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6','n7')]
c['entries'].append({'id':'n8','role':'note','body':'R8: board.md:3 Thread A resolved; :4 Thread B cause UPSTREAM_RATE_LIMIT; :5 Thread C notify-worker ongoing cause unknown. changes.md:3 CHG-159 PROPOSED. notify-worker.log:5,45,50,58,65,72 config validation failed key http.* (BAD_CONFIG via CHG-120 r02 changes.md:4). checkout-api.log:1,6,20,29,35,39,49,51,54 429; payments-svc.log:2,24,25,34,39,41,45,46,52 429. Next: advance to R9.'})
json.dump(c,open(p,'w'))
print('ok')