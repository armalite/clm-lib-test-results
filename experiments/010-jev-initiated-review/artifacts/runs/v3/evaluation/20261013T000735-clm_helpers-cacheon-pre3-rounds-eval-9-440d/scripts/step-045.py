import json
p='/task/workspace/context.json'
c=json.load(open(p))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']=n['body'].replace('\nR9 released (board 3 lines). Next: inspect r9 board/logs.','')
n['body']+="\nR9: board Thread C note pods restarting, investigation continues (round-09/board.md:3). search-api config validation failed http.max_inflight=-1 round-09/logs/search-api.log:2,14,18,20,23,24,33. disk high notify-worker round-09/logs/notify-worker.log:4,8; shipping round-09/logs/shipping-svc.log:8,13. no DNS. Next: advance to round 10."
c['entries']=[n]
json.dump(c,open(p,'w'))
print('ok')