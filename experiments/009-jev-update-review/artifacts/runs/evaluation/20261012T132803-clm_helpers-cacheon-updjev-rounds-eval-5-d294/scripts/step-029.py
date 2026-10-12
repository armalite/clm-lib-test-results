import json,re
for s in ['auth-svc','checkout-api','ledger-svc','search-api','shipping-svc']:
    L=open(f'/task/fixtures/round-11/logs/{s}.log').read().splitlines()
    h=[(i+1,l[:110]) for i,l in enumerate(L) if re.search('ERROR|WARN|FATAL',l) and 'slow' not in l]
    print(s,len(h),h[:2],h[-1:] if h else '')
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
b=c['entries'][0]['body'].replace('\nNEXT: advance to R11.','')
b+='\nR11: board.md:3 Thread B adds ledger-svc; :4 Thread B MITIGATED; :5 Thread C ongoing; :6 CLOSED CUSTOMER_COMMS. CHG-179 PROPOSED ignore.\nOpen followups: DATA_BACKFILL,VENDOR_TICKET,CAPACITY_REVIEW,ALERT_TUNING.\nNEXT: check R11 logs then advance R12.'
c['entries'][0]['body']=b
json.dump(c,open('/task/workspace/context.json','w'))