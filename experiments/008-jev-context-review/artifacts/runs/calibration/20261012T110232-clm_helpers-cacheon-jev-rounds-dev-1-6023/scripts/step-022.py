import subprocess
print(subprocess.run(['python3','/task/workspace/scan.py','08'],capture_output=True,text=True).stdout[:5000])