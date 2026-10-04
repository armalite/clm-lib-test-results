code='''"""Invoice calculator."""
from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')
def r2(x): return x.quantize(Q, rounding=ROUND_HALF_UP)

def _validate(lines):
    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')
        try: p=Decimal(str(l['unit_price']))
        except Exception: raise ValueError('price')
        if not p.is_finite() or p<0: raise ValueError('price')

def tax_rate(customer): return Decimal('0.10')

def compute_invoice(lines, customer):
    _validate(lines)
    amounts=[r2(l['qty']*Decimal(str(l['unit_price']))) for l in lines]
    subtotal=sum(amounts,Decimal(0))
    discounts=[]
    discount=sum((r2(d) for d in discounts),Decimal(0))
    shipping=Decimal(0)
    tax=r2((subtotal-discount)*tax_rate(customer))
    total=subtotal-discount+shipping+tax
    return {k:str(r2(v)) for k,v in [('subtotal',subtotal),('discount',discount),('shipping',shipping),('tax',tax),('total',total)]}
'''
open('/task/workspace/invoice/core.py','w').write(code)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 done: core.py has r2, _validate, tax_rate(10%), compute_invoice with discounts list, shipping 0. Read stage files for reqs.'}]},open('/task/workspace/context.json','w'))