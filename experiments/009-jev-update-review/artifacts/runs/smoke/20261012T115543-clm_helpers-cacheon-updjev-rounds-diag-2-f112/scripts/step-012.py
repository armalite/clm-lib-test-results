import json
c=json.load(open('/task/workspace/context.json'))
b=[e for e in c['entries'] if e['id']=='notes'][0]['body']+' R3 inventory-svc logs: NO cache misses; disk usage high /var/data 91-97% (inventory-svc.log:7,8,29,80) -> likely DISK_PRESSURE not CACHE_STAMPEDE. Next: advance to R4.'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':b}]},open('/task/workspace/context.json','w'))
print('ok')