import json
e=[]
def a(i,b):e.append({'id':i,'role':'note','body':b})
a('n1','R1: CHG-111 PROPOSED round-01/changes.md:3; CHG-113 APPLIED round-01/changes.md:4 checkout-api feature.batch_size=0 (BAD_CONFIG candidate, no errors yet); CHG-114 APPLIED :5 inventory-svc. slow query WARN = noise.')
a('n2','R2: round-02/board.md:3 OPEN VENDOR_TICKET; :4 OPEN POSTMORTEM_DRAFT.')
a('n3','R3: round-03/board.md:3 Thread A UPSTREAM_RATE_LIMIT pricing-svc+search-api; logs round-03/logs/pricing-svc.log:4-64, search-api.log:8-79.')
a('n4','R4: round-04/board.md:3 Thread B inventory-svc; :4 OPEN CAPACITY_REVIEW.')
a('n6','R6: round-06/board.md:3 Thread A mitigated; :4 CLOSED VENDOR_TICKET; round-06/changes.md:4 CHG-150 APPLIED.')
a('n7','R7: round-07/board.md:3 Thread B = DNS_RESOLUTION inventory-svc (SERVFAIL kms.internal round-07/logs/inventory-svc.log:1-73). :4 Thread D MEMORY_LEAK pricing-svc (heap round-07/logs/pricing-svc.log:8-69). CHG-153 PROPOSED.')
a('n8','R8: round-08/board.md:3 Thread A resolved; :4 OPEN DATA_BACKFILL. CHG-157 APPLIED log sampling (noise). inventory DNS still failing round-08/logs/inventory-svc.log:6; pricing heap round-08/logs/pricing-svc.log:4. Next: advance R9.')
json.dump({'format':'clm-context/v1','entries':e},open('/task/workspace/context.json','w'))