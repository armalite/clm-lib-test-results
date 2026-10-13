import json
p='/task/workspace/context.json'
c=json.load(open(p))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+="\nR7: board Thread B cause revised DISK_PRESSURE (round-07/board.md:3); Thread D closed false alarm (round-07/board.md:4); follow-up CLOSED POSTMORTEM_DRAFT (round-07/board.md:5). changes: CHG-149 PROPOSED only (round-07/changes.md:3). notify-worker disk high round-07/logs/notify-worker.log:2,3,6; shipping hits round-07/logs/shipping-svc.log (check disk lines). No DNS errors listed. Next: advance to round 8."
c['entries']=[n]
json.dump(c,open(p,'w'))
print('ok')