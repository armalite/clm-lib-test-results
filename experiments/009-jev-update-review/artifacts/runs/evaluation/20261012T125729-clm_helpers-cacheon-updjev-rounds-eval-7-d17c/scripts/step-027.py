import json,re
L=open('/task/fixtures/round-10/logs/ledger-svc.log').read().splitlines()
h=[i+1 for i,l in enumerate(L) if re.search(r'config validation|pool|OOM|restart',l,re.I)]
print(h[:20]);print(L[h[0]-1][:200] if h else '')
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]['body'].replace(' NEXT: advance to R10.','')
n+=' R10: board:3 Thread B MITIGATED; board:4 Thread C still restarting; board:5 CLOSED RUNBOOK_UPDATE. R10 ledger hits lines '+','.join(map(str,h[:10]))+'. NEXT: advance to R11.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))