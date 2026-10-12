import json,re
for i,l in enumerate(open('/task/fixtures/round-08/logs/checkout-api.log'),1):
  if re.search('pool|ERROR',l): print(i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]['body'].replace(' NEXT: advance to R8.','')
n+="\nR8: board says Thread D closed false alarm (round-08/board.md:3) - verify vs logs. CHG-156 PROPOSED ignore."
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))