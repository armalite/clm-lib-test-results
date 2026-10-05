import json,subprocess,sys
src='''from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def discount_rate(lines, customer, subtotal):
    return TIER.get(customer.get('tier'), Decimal('0'))

def tax_rate(lines, customer):
    return Decimal('0')

def validate(lines, customer):
    if not lines:
        raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError('qty')
        try:
            p=Decimal(str(l.get('unit_price')))
        except Exception:
            raise ValueError('price')
        if not p.is_finite() or p<0:
            raise ValueError('price')

def compute_invoice(lines, customer):
    validate(lines, customer)
    sub=sum((_r(l['qty']*Decimal(str(l['unit_price']))) for l in lines), Decimal('0'))
    disc=_r(sub*discount_rate(lines,customer,sub))
    tax=_r((sub-disc)*tax_rate(lines,customer))
    tot=sub-disc+tax
    return {k:str(_r(v)) for k,v in (('subtotal',sub),('discount',disc),('tax',tax),('total',tot))}

def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(src)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 done: invoice/core.py implements compute_invoice (round lines half-up, tier gold5%/silver2%, validation qty pos int, price>=0, nonempty). Hooks discount_rate(lines,customer,sub), tax_rate(lines,customer), validate. format_money(amount,currency) stub NotImplemented (exported in __init__). Tests at /task/fixtures/current-tests.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))