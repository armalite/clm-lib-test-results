import subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("        if q>=100: a*=Decimal('0.90')\n","        if q>=200: a*=Decimal('0.88')\n        elif q>=50: a*=Decimal('0.95')\n")
s+='''
CUR={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in CUR: raise ValueError('bad currency')
    try: d=Decimal(str(amount))
    except Exception: raise ValueError('bad amount')
    d=r(d)
    sign='-' if d<0 else ''
    return sign+CUR[currency]+str(abs(d))
'''
open(p,'w').write(s)
open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice, format_money\n')
open('/task/workspace/NOTES.md','w').write('stage1-3 done in core.py (tiers plat10 gold7 silver3, tax10%, validation, bulk 200->.88 50->.95, format_money)\n')
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])