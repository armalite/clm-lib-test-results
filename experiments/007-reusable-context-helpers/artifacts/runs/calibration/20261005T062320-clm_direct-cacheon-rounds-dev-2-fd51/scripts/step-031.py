import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1':e['body']+="\nR10: Thread D false alarm closed (round-10/board.md:3) -> 429s not incident. DATA_BACKFILL CLOSED (board:4). CHG-175 noise. search config validation lines 1,4,7,8,20,30,50,54; CERT auth round-10/logs/auth-svc.log:10,17; shipping round-10/logs/shipping-svc.log:3,60. Next: advance R11."
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))