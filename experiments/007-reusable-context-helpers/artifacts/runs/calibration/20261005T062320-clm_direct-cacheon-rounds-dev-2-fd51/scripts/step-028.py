import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1':e['body']+="\nR9: board Thread C note pods restarting (round-09/board.md:3). CHG-166 noise. search-api config validation lines 2,9,13,19,25,26; 429 lines 1,5,11,20. CERT auth round-09/logs/auth-svc.log:22,55; shipping round-09/logs/shipping-svc.log:28,56. Next: advance R10."
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))