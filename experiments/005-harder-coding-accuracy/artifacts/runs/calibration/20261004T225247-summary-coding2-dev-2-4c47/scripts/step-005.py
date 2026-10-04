code='''from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')
def r2(x): return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def _validate(lines):
    if not lines: raise ValueError('empty lines')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('bad qty')
        try: p=Decimal(str(l['unit_price']))
        except Exception: raise ValueError('bad price')
        if not p.is_finite() or p<0: raise ValueError('negative price')

def compute_invoice(lines, customer):
    _validate(lines)
    amounts=[r2(int(l['qty'])*Decimal(str(l['unit_price']))) for l in lines]
    subtotal=sum(amounts,Decimal('0'))
    tier_disc=r2(TIER.get(customer.get('tier'),Decimal('0'))*subtotal)
    discount=tier_disc
    shipping=Decimal('7.50') if subtotal-discount<Decimal('100.00') else Decimal('0')
    tax=r2((subtotal-discount)*Decimal('0'))
    total=subtotal-discount+shipping+tax
    return {k:str(r2(v)) for k,v in [('subtotal',subtotal),('discount',discount),('shipping',shipping),('tax',tax),('total',total)]}
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/NOTES.md','a').write('stage2 done: validation, shipping 7.50 if sub-disc<100\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])