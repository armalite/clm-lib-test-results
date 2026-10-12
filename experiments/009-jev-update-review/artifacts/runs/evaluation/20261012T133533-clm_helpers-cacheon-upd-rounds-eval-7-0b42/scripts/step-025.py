import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
c['entries'][0]['body']+=' R10: B mitigated (round-10/board.md:3); C still restarting (r10 board.md:4); RUNBOOK_UPDATE CLOSED (r10 board.md:5).'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')