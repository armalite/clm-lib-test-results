import subprocess,sys
print(open('/task/workspace/exporter/core.py').read())
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-500:])