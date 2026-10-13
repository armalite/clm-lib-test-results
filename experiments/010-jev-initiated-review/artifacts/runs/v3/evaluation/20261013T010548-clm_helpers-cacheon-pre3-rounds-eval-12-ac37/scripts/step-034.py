import json
c=json.load(open('/task/workspace/context.json'))
n1=[e for e in c['entries'] if e['id']=='n1'][0]
n1['body']=n1['body'].replace(' R8 pricing-svc log errors not yet inspected (grep non-slow-query lines).',' R8 pricing-svc.log:5-83 ERROR config validation failed cache.ttl_s=-1 build 3.22.4 (confirms BAD_CONFIG_ROLLOUT via CHG-113).\nNext: advance to round 9.')
json.dump({'format':'clm-context/v1','entries':[n1]},open('/task/workspace/context.json','w'))
print('ok')