import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id']=='n1'][0]
e['body']+='\nR8: board round-08/board.md:3 Thread A resolved; :4 Thread B mitigated; :5 Thread C search-api ongoing cause unknown; :6 VENDOR_TICKET CLOSED. changes.md:3 CHG-159 retry. search-api ERROR config validation failed http.max_inflight round-08/logs/search-api.log:9-75 n=7 (=> BAD_CONFIG via CHG-120 round-02/changes.md:4). other svcs 0 errs.'
c['entries']=[e]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')