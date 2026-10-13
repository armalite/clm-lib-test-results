import subprocess
print(open('/task/workspace/exporter/core.py').read()[:3500])
print(subprocess.run(['grep','-n','def ','/task/workspace/regtool.py'],capture_output=True,text=True).stdout)