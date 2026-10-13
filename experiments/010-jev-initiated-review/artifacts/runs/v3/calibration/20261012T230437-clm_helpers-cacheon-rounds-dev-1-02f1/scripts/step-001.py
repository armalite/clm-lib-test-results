import os
for r,d,f in os.walk('/task/fixtures/round-01'):
  for x in f:
    p=os.path.join(r,x);print(p,sum(1 for _ in open(p)))
print(open('/task/fixtures/round-01/board.md').read()[:1500])
import subprocess
print(subprocess.run('grep -niE "error|warn|fail" -r /task/fixtures/round-01/logs | head -30',shell=True,capture_output=True,text=True).stdout[:3000])