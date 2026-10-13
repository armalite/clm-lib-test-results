import json
e=json.load(open('/task/workspace/context.json'))['entries']
e=[x for x in e if x['id'].startswith('n')]
e.append({'id':'n11','role':'note','body':'R11: round-11/board.md:3 Thread B mitigated; :4 Thread C still ongoing (checkout batch_size=0 errors round-11/logs/checkout-api.log:2-64). Next: advance R12.'})
json.dump({'format':'clm-context/v1','entries':e},open('/task/workspace/context.json','w'))