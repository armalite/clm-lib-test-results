s=open('/task/workspace/invoice/core.py').read()
s=s.replace("        if q>=100: a*=Decimal('0.90')","        if q>=200: a*=Decimal('0.88')\n        elif q>=50: a*=Decimal('0.95')")
s+='''
PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in PFX: raise ValueError('currency')
    d=r2(Decimal(str(amount)))
    sign='-' if d<0 else ''
    return sign+PFX[currency]+str(abs(d))
'''
open('/task/workspace/invoice/core.py','w').write(s)
open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice, format_money\n')
open('/task/workspace/NOTES.md','a').write('stage3: format_money, bulk >=200 x0.88 elif >=50 x0.95\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])