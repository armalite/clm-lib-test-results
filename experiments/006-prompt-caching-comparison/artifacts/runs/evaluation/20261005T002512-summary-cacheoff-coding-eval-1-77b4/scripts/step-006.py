code='''from decimal import Decimal, ROUND_HALF_EVEN, InvalidOperation

Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def _bulk(qty):
    if qty>=200: return Decimal('0.88')
    if qty>=50: return Decimal('0.95')
    return Decimal('1')

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty lines')
    sub=Decimal('0')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('bad qty')
        try: p=Decimal(str(l['unit_price']))
        except (InvalidOperation,KeyError): raise ValueError('bad price')
        if not p.is_finite() or p<0: raise ValueError('negative price')
        sub+=Decimal(q)*p*_bulk(q)
    rate=TIER.get((customer or {}).get('tier'),Decimal('0'))
    disc=sub*rate
    tax=(sub-disc)*Decimal('0.10')
    rs,rd,rt=r2(sub),r2(disc),r2(tax)
    tot=rs-rd+rt
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(r2(tot))}

def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/NOTES.md','a').write('Stage3 done: tier disc gold5 silver2, exact calc then half-even round.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])