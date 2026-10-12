import json
d=json.load(open('/task/workspace/context.json'))
b=[e for e in d['entries'] if e['id']=='n1'][0]['body']
b=b.replace(' Next: advance to round 9.','')
b+='\nRound9: board.md:3 Thread B mitigated; board.md:4 Thread C pods still restarting (ongoing). changes.md:3 CHG-164 APPLIED retry budget (irrelevant). notify-worker config validation failed lines 3,5,12,14,15,48,52,63,67. checkout 429 34,55; payments 429 34,42; auth/search clean. Next: advance to round 10.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':b}]},open('/task/workspace/context.json','w'))
print('ok')