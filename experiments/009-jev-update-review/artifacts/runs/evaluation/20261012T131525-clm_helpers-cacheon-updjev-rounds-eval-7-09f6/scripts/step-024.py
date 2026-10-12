import json,re
L=open('/task/fixtures/round-09/logs/ledger-svc.log').read().splitlines()
h=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|pool|refused|timeout',l,re.I)]
print(len(h),h[:15])
for i in h[:4]: print(i,L[i-1][:220])
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]['body']
n+=' R8 logs: disk checkout-api.log:1-73, payments-svc.log:2-40. R9: board.md:3 Thread A resolved; board.md:4 Thread B cause revised DISK_PRESSURE (checkout-api+payments-svc); board.md:5 Thread C ledger-svc failures cause unknown ongoing (suspect CHG-113 pool_max=0); board.md:6 OPEN VENDOR_TICKET; CHG-163 irrelevant.'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open('/task/workspace/context.json','w'))