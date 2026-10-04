p='/task/workspace/invoice/core.py'
s=open(p).read()
s+='\n\ndef format_money(amount, currency):\n    raise NotImplementedError\n'
open(p,'w').write(s)
open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice, format_money\n__all__=["compute_invoice","format_money"]\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-300:])