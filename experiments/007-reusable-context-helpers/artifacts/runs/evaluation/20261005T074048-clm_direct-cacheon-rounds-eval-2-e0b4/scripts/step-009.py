import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2')]
c['entries'].append({'id':'n3','role':'note','body':'R3: Follow-up CLOSED CUSTOMER_COMMS (round-03/board.md:3). CHG-121 APPLIED retry budget GETs=1 (round-03/changes.md:3). No ERROR lines R3. Next: advance to R4.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')