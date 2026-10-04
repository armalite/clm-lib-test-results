open('/task/workspace/invoice/core.py','a').write('\ndef format_money(amount, currency):\n    raise NotImplementedError\n')
open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice, format_money\n__all__=["compute_invoice","format_money"]\n')
open('/task/workspace/NOTES.md','w').write('Stage1 done: core.py has r(), TIER, discount_rate(customer,sub,lines), tax_rate(customer), validation. format_money stub (from skeleton).\n')
import subprocess,sys
p=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(p.stderr[-300:])