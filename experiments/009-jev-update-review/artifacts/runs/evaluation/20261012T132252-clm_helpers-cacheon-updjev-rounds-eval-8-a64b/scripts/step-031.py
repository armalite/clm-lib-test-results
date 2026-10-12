import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if not e['id'].startswith(('s29','s30'))]
c['entries'].append({'id':'n11','role':'note','body':'R11 board: B mitigated (round-11/board.md:3); C still restarting, ongoing (round-11/board.md:4). CHG-182 irrelevant. Next: advance to R12.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')