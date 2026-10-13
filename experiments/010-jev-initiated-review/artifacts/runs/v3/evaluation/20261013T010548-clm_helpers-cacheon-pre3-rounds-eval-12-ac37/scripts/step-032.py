import json
c=json.load(open('/task/workspace/context.json'))
n1=[e for e in c['entries'] if e['id']=='n1'][0]
b=n1['body'].replace('\nNext: advance to round 8.','')
b+='\nR8: board.md:3 Thread A resolved; board.md:4 Thread B cause UPSTREAM_RATE_LIMIT (supersedes queue); board.md:5 Thread C pricing-svc failures cause unknown ongoing (suspect CHG-113 ttl=-1). R8 pricing-svc log errors not yet inspected (grep non-slow-query lines).'
n1['body']=b
json.dump({'format':'clm-context/v1','entries':[n1]},open('/task/workspace/context.json','w'))
L=open('/task/fixtures/round-08/logs/pricing-svc.log').read().splitlines()
for i,l in enumerate(L):
  if 'ERROR' in l: print(i+1,l[:160])