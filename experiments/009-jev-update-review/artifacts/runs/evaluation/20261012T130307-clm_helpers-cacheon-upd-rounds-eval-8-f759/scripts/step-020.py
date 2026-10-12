import json,subprocess
d=json.load(open('/task/workspace/context.json'))
n=[e for e in d['entries'] if e['id']=='n1'][0]
n['body']=n['body'].replace(' Open:',' R10: board.md:3 B adds payments-svc; board.md:4 Thread C notify-worker failures ongoing cause unknown (CHG-113 pool_max=-4?); board.md:5 OPEN DATA_BACKFILL; board.md:6 OPEN POSTMORTEM_DRAFT; changes.md:3 CHG-173 dashboards. Open:')
json.dump({'format':'clm-context/v1','entries':[n]},open('/task/workspace/context.json','w'))
r=subprocess.run('grep -n -i "pool\\|config\\|invalid\\|err" /task/fixtures/round-10/logs/notify-worker.log | head -15',shell=True,capture_output=True,text=True)
print(r.stdout[:2000])