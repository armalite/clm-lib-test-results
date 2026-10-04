src=open('/task/workspace/invoice/core.py').read()
src=src.replace('    tax=(sub-disc)*Decimal("0.10")','    TR={"NZ":Decimal("0.15"),"AU":Decimal("0.10"),"US":Decimal("0")}\n    tax=(sub-disc)*TR.get(customer.get("region"),Decimal("0.12"))\n    if customer.get("tax_exempt") is True: tax=Decimal(0)')
src+='''
PREFIX={"NZD":"NZ$","AUD":"A$","USD":"US$"}
def format_money(amount, currency):
    if currency not in PREFIX: raise ValueError("bad currency")
    d=r2(Decimal(str(amount)))
    s="-" if d<0 else ""
    return s+PREFIX[currency]+str(abs(d))
'''
open('/task/workspace/invoice/core.py','w').write(src)
open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice, format_money\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])