code='''from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')
def r(x): return x.quantize(Q, rounding=ROUND_HALF_UP)

def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    sub=Decimal(0)
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<=0: raise ValueError('qty')
        p=Decimal(str(l['unit_price']))
        if p<0: raise ValueError('price')
        sub+=r(q*p)
    disc=Decimal(0)
    ship=Decimal(0)
    tax=r((sub-disc)*Decimal('0.10'))
    tot=sub-disc+ship+tax
    return {k:str(r(v)) for k,v in [('subtotal',sub),('discount',disc),('shipping',ship),('tax',tax),('total',tot)]}
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/NOTES.md','w').write('stage1: rounding half up per line/discount/tax; validation; tax 10%. impl in core.py\n')
import subprocess,sys
p=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(p.stderr[-1500:])