import subprocess,sys,re
t=open('/task/fixtures/current-tests/test_invoice.py').read()
for i,l in enumerate(t.splitlines()):
  if 'format_money' in l: print(i,l)
open('/task/workspace/invoice/core.py','a').write('\ndef format_money(x):\n    return str(r2(Decimal(str(x))))\n')
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])