import subprocess,json
r='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  print(f);print(subprocess.run(['cat','-n',r+f],capture_output=True,text=True).stdout)
print(subprocess.run('grep -nvE "slow query| INFO " -r '+r+'logs | head -30',shell=True,capture_output=True,text=True).stdout[:3000])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))