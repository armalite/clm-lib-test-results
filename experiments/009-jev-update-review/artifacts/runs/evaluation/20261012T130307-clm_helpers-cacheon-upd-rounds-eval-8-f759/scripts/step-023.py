import json
d=json.load(open('/task/workspace/context.json'))
n=[e for e in d['entries'] if e['id']=='n1'][0]
n['body']=n['body'].replace('Next: advance to R11.','R11: board.md:3 B mitigated; board.md:4 C still ongoing; changes.md:3 CHG-182 retry budget (irrelevant). Next: advance to R12.')
json.dump({'format':'clm-context/v1','entries':[n]},open('/task/workspace/context.json','w'))
print('ok')