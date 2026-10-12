import json,re
L=open('/task/fixtures/round-09/logs/ledger-svc.log').read().splitlines()
h=[f'{i+1}:{l[:110]}' for i,l in enumerate(L) if re.search(r'(?i)error|pool|fail',l)]
print(len(h));print('\n'.join(h[:8]))
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]['body'].replace(' NEXT: advance to R9.','')+' R9: board:3 Thread A RESOLVED; board:4 Thread B cause revised DISK_PRESSURE (checkout-api+payments-svc, ongoing); board:5 Thread C ledger-svc failures cause unknown ongoing (likely CHG-113 pool_max=0 BAD_CONFIG_ROLLOUT); board:6 OPEN VENDOR_TICKET; changes:3 CHG-163 noise.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))