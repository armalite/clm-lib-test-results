code='''"""Invoice core."""
from decimal import Decimal, ROUND_HALF_EVEN

Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)
DISC={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty lines')
    subtotal=Decimal('0')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('bad qty')
        try: p=Decimal(str(l['unit_price']))
        except Exception: raise ValueError('bad price')
        if not p.is_finite() or p<0: raise ValueError('negative price')
        amt=Decimal(q)*p
        if q>=200: amt*=Decimal('0.88')
        elif q>=50: amt*=Decimal('0.95')
        subtotal+=amt
    discount=subtotal*DISC.get((customer or {}).get('tier'),Decimal('0'))
    tax=(subtotal-discount)*Decimal('0.10')
    s,d,t=r2(subtotal),r2(discount),r2(tax)
    total=s-d+t
    return {'subtotal':str(s),'discount':str(d),'tax':str(t),'total':str(r2(total))}

def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/NOTES.md','a').write('Stage3: tier discount gold5 silver2; no line rounding, exact then half-even round s,d,t; total from rounded.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])