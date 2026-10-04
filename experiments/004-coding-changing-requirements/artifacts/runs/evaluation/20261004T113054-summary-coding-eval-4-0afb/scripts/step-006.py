import subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("        if l['qty']>=100: a*=Decimal('0.90')\n","        if l['qty']>=200: a*=Decimal('0.88')\n        elif l['qty']>=50: a*=Decimal('0.95')\n")
s+='''
CUR={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in CUR: raise ValueError('currency')
    d=r(Decimal(str(amount)))
    sign='-' if d<0 else ''
    return sign+CUR[currency]+str(abs(d))
'''
open(p,'w').write(s)
open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice, format_money\n')
open('/task/workspace/NOTES.md','a').write('stage3 done: bulk 200->.88/50->.95, format_money\n')
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])