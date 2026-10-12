import json
b=open('/task/workspace/context.json').read()
d=json.load(open('/task/workspace/context.json'))
n=[e for e in d['entries'] if e['id']=='n1'][0]
n['body']=n['body'].replace(' Open:',' R9: board.md:3 follow-up OPEN RUNBOOK_UPDATE. Open:')
json.dump({'format':'clm-context/v1','entries':[n]},open('/task/workspace/context.json','w'))
import subprocess
print(subprocess.run(['grep','-n','-i','pool\\|error\\|config','/task/fixtures/round-09/logs/notify-worker.log'],capture_output=True,text=True).stdout[:1500])