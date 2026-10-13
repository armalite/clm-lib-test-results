import json
d=json.load(open('/task/workspace/context.json'))
n=[e for e in d['entries'] if e['id']=='n1'][0]['body']
n+='\nR7: board.md:3 Thread B cause revised DISK_PRESSURE; board.md:4 Thread D closed false alarm; board.md:5 CLOSED POSTMORTEM_DRAFT. changes.md:3 CHG-149 PROPOSED only. disk notify-worker.log:2-56, shipping-svc.log:18-80; no cert errors now; others clean. Next: advance R8.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))
print('ok')