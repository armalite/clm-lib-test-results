src='''from decimal import Decimal, ROUND_HALF_EVEN

Q=Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)

TIERS={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError('bad qty')
        if Decimal(str(l['unit_price']))<0:
            raise ValueError('negative price')
    subtotal=Decimal('0')
    for l in lines:
        amt=Decimal(l['qty'])*Decimal(str(l['unit_price']))
        if l['qty']>=200:
            amt*=Decimal('0.88')
        elif l['qty']>=50:
            amt*=Decimal('0.95')
        subtotal+=amt
    rate=TIERS.get(customer.get('tier'),Decimal('0'))
    discount=subtotal*rate
    tax=(subtotal-discount)*Decimal('0.10')
    s,d,t=r2(subtotal),r2(discount),r2(tax)
    return {'subtotal':str(s),'discount':str(d),'tax':str(t),'total':str(r2(s-d+t))}


def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(src)
open('/task/workspace/NOTES.md','a').write('Stage3: tier gold5 silver2; no line rounding, exact then half-even round s,d,t.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])