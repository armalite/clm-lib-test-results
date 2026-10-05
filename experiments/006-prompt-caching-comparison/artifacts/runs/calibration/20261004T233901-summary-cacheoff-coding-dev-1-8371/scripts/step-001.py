import subprocess
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
print(subprocess.run('ls -R /task/workspace /task/fixtures/current-tests; cat /task/workspace/invoice/*.py',shell=True,capture_output=True,text=True).stdout)