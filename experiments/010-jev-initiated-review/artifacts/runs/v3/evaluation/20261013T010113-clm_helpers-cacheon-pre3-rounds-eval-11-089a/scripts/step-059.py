import json
ctx=json.load(open('/task/workspace/context.json'))
ctx['entries']=[e for e in ctx['entries'] if e['id'].startswith('n')]
json.dump(ctx,open('/task/workspace/context.json','w'))
print('ok')