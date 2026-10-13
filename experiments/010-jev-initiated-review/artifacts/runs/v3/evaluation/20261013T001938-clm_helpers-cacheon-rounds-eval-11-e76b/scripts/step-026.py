import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='notes': e['body']+='\nR9: board.md:3 Thread D closed false alarm (not incident). inventory-svc.log:7-80 DNS SERVFAIL continues. pricing/search/checkout clean; shipping only slow-query noise.'
c['entries']=[e for e in c['entries'] if e['id']=='notes']
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')