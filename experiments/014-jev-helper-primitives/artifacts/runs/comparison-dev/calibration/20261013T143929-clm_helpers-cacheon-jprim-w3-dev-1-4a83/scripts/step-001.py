import subprocess
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
print(subprocess.run('ls -R /task/workspace /task/fixtures; cat /task/workspace/exporter/*.py | head -50',shell=True,capture_output=True,text=True).stdout)