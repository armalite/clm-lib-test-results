import os,subprocess
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
for r,d,f in os.walk('/task/workspace/invoice'):print(r,f)
print(subprocess.run('ls /task/fixtures/current-tests; cat /task/workspace/invoice/*.py | head -50',shell=True,capture_output=True,text=True).stdout)