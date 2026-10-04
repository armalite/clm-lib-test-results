code='''from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')
def r(x): return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def validate(lines):
    if not lines: raise ValueError('empty lines')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('bad qty')
        try: p=Decimal(str(l['unit_price']))
        except Exception: raise ValueError('bad price')
        if not p.is_finite() or p<0: raise ValueError('negative price')

def compute_invoice(lines, customer):
    validate(lines)
    amounts=[r(Decimal(l['qty'])*Decimal(str(l['unit_price']))) for l in lines]
    subtotal=sum(amounts,Decimal(0))
    discount=r(TIER.get(customer.get('tier'),Decimal(0))*subtotal)
    shipping=Decimal('7.50') if subtotal-discount<Decimal(100) else Decimal(0)
    tax=r((subtotal-discount)*Decimal(0))
    total=subtotal-discount+shipping+tax
    return {k:str(r(v)) for k,v in dict(subtotal=subtotal,discount=discount,shipping=shipping,tax=tax,total=total).items()}
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/NOTES.md','a').write('stage2 done: validation, shipping 7.50 if subtotal-discount<100\n')
import subprocess,sys
p=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(p.stderr[-1500:])