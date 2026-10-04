s=open('/task/workspace/invoice/core.py').read()
s=s.replace("    tax=(sub-disc)*Decimal('0.10')","    tr=TAX.get(customer.get('region'),Decimal('0.12'))\n    if customer.get('tax_exempt') is True: tr=Decimal(0)\n    tax=(sub-disc)*tr")
s=s.replace("def compute_invoice","TAX={'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal(0)}\nPFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}\ndef format_money(amount, currency):\n    if currency not in PFX: raise ValueError('currency')\n    d=r(Decimal(str(amount)))\n    neg=d<0\n    return ('-' if neg else '')+PFX[currency]+str(abs(d))\ndef compute_invoice",1)
open('/task/workspace/invoice/core.py','w').write(s)
open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice, format_money\n')
import subprocess,sys
p=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(p.stderr[-1500:])