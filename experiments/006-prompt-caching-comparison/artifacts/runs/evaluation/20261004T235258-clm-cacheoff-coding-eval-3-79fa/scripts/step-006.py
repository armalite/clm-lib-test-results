import subprocess
print(subprocess.run(['grep','-n','','/task/workspace/invoice/core.py'],capture_output=True,text=True).stdout[-3000:])