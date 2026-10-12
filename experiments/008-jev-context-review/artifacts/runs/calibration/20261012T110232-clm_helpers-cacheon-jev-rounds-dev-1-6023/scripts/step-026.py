import json,subprocess
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))
r=subprocess.run(['python3','/task/workspace/scan.py','09'],capture_output=True,text=True)
print(r.stdout[:3500]);print(r.stderr[:300])