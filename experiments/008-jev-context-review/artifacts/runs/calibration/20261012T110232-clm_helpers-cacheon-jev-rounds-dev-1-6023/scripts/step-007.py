import json,subprocess
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2')]
json.dump(c,open('/task/workspace/context.json','w'))
print(subprocess.run(['python3','/task/workspace/scan.py','03'],capture_output=True,text=True).stdout[:4000])