import subprocess
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
print(subprocess.run('ls -R /task/workspace /task/fixtures; cat /task/workspace/exporter/*.py; head -c 2500 /task/fixtures/current-tests/test_stage.py',shell=True,capture_output=True,text=True).stdout)