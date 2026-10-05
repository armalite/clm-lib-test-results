import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=" | R6: board.md:3 CLOSED CUSTOMER_COMMS. CHG-147 APPLIED TLS ticket rotation (irrelevant). checkout heap WARN checkout-api.log:17-66 (no 429). search-api.log:6-74 disk 91-97%. R6 done -> advance next."
json.dump(c,open('/task/workspace/context.json','w'))