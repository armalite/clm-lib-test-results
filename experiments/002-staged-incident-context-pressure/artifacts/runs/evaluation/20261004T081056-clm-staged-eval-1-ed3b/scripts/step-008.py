import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' changes.log:2 CHG-5118 REVERTED catalog-api; :3 CHG-5119 PROPOSED profile-svc (irrelevant). Next: advance to stage3.'
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/stage-2/metrics/quotes-api.csv').read()[:500])