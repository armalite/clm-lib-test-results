for n,l in enumerate(open('/task/workspace/invoice/core.py'),1):
  if n>=26: print(n,l.rstrip())
import subprocess,sys
r=subprocess.run([sys.executable,'-c','from invoice import format_money as f\ntry: f("1","EUR")\nexcept ValueError: print("VE ok")\nprint(f("-1234.5","NZD"))'],cwd='/task/workspace',capture_output=True,text=True);print(r.stdout,r.stderr[-500:])
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-300:])