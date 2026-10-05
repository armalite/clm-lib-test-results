src='''from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty lines')
    sub=Decimal('0')
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<=0:
            raise ValueError('bad qty')
        p=Decimal(str(l['unit_price']))
        if p<0:
            raise ValueError('negative price')
        sub+=_r(q*p)
    sub=_r(sub)
    disc=_r(sub*TIER.get(customer.get('tier'),Decimal('0')))
    taxrate=Decimal('0')
    tax=_r((sub-disc)*taxrate)
    total=sub-disc+tax
    return {k:str(_r(v)) for k,v in (('subtotal',sub),('discount',disc),('tax',tax),('total',total))}


def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(src)
open('/task/workspace/NOTES.md','w').write('stage1 done: rounding half-up per line, tier gold5 silver2, validation. tax rate 0.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])