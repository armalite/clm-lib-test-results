import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6')]
c['entries'].append({'id':'n7','role':'note','body':'R7: board.md:3 Thread B affected services now include checkout-api (cause QUEUE_BACKLOG per board, status ongoing unchanged). changes.md:3 CHG-152 PROPOSED only. checkout-api.log 429 tax-provider 4,14,15 (10 errs); ledger-svc.log 429 tax-provider 13,20,34 (8 errs). inventory/search/pricing 0 errs. Thread B likely really UPSTREAM_RATE_LIMIT ledger+checkout. Open follow-ups: CAPACITY_REVIEW,RUNBOOK_UPDATE,POSTMORTEM_DRAFT,CUSTOMER_COMMS,ALERT_TUNING. Next: advance to round 8.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')