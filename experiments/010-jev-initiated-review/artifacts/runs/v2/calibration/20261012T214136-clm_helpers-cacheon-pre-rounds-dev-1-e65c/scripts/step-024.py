import json
d=json.load(open('/task/workspace/context.json'))
b=[e for e in d['entries'] if e['id']=='n1'][0]['body']
b=b.replace(' Next: inspect r5 non-slow-query errors, then advance.','')
b+=' r5 checked: only payments 429 fx-rates (13,19..73); notify clean.\nRound6: board.md:3 CLOSED ALERT_TUNING; board.md:4 OPEN CUSTOMER_COMMS. changes.md:3 CHG-147 APPLIED retry budget GETs=1 (irrelevant?). checkout-api 429 fx-rates lines 19,30,56..77; payments-svc 429 3..76; auth/search/notify clean. Next: advance to round 7.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':b}]},open('/task/workspace/context.json','w'))
print('ok')