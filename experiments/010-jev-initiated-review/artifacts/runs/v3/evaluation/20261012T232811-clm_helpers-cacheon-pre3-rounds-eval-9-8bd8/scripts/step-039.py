import json
e=json.load(open('/task/workspace/context.json'))['entries']
keep=[x for x in e if x['id'].startswith('n')]
json.dump({'format':'clm-context/v1','entries':keep},open('/task/workspace/context.json','w'))
print(len(keep))