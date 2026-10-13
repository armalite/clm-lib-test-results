import subprocess
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
print(subprocess.run('ls -R /task/workspace/exporter; cat /task/workspace/exporter/*.py',shell=True,capture_output=True,text=True).stdout[:2500])