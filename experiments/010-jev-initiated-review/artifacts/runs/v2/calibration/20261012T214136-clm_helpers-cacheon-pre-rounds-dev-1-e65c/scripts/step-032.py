import json
d=json.load(open('/task/workspace/context.json'))
b=[e for e in d['entries'] if e['id']=='n1'][0]['body']
b=b.replace(' Next: advance to round 8.','')
b+='\nRound8: board.md:3 Thread A resolved; board.md:4 Thread B revised UPSTREAM_RATE_LIMIT; board.md:5 Thread C notify-worker ongoing cause unknown. changes.md:3 CHG-159 PROPOSED. notify-worker.log config validation failed http.max_inflight=0 build 8.56.0 lines 5,45,50,58,65,72 -> BAD_CONFIG_ROLLOUT from CHG-120 (r02 changes.md:4). checkout 429 1..54; payments 429 2..83; auth/search clean. Next: advance to round 9.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':b}]},open('/task/workspace/context.json','w'))
print('ok')