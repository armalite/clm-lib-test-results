import json
c=json.load(open('/task/workspace/context.json'))
n1=[e for e in c['entries'] if e['id']=='n1'][0]
n1['body']=n1['body'].replace('Next: advance to round 9.','R9: board.md:3 Thread B mitigated; board.md:4 Thread C pods restarting, ongoing; board.md:5 CLOSED RUNBOOK_UPDATE; changes.md:3 CHG-164 APPLIED retry budget. 429 tax-provider checkout-api.log:10-66; pricing-svc.log:69 config validation failed ttl=-1.\nNext: advance to round 10.')
json.dump({'format':'clm-context/v1','entries':[n1]},open('/task/workspace/context.json','w'))
print('ok')