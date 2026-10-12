import json,re
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]['body']
n+=' R10: board.md:3 Thread B mitigated; board.md:4 Thread C still restarting ongoing; board.md:5 CLOSED RUNBOOK_UPDATE.'
L=open('/task/fixtures/round-10/logs/ledger-svc.log').read().splitlines()
h=[i+1 for i,l in enumerate(L) if 'pool_max' in l]
n+=' R10 ledger pool_max hits '+str(h[:6])+'..'+str(h[-1:] if h else '')
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open('/task/workspace/context.json','w'))
print(h[:6],h[-1:])