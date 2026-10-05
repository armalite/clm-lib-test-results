import json,subprocess,sys
code='''from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def compute_invoice(lines, customer):
    sub=Decimal(0)
    for l in lines:
        a=Decimal(l['qty'])*Decimal(l['unit_price'])
        if l['qty']>=100: a*=Decimal('0.90')
        sub+=r2(a)
    disc=r2(sub*TIER.get(customer.get('tier'),Decimal(0)))
    rate=Decimal(0)
    tax=r2((sub-disc)*rate)
    tot=sub-disc+tax
    return {k:str(r2(v)) for k,v in (('subtotal',sub),('discount',disc),('tax',tax),('total',tot))}


def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(code)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-800:])
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 done: invoice/core.py has compute_invoice (line round half-up, bulk qty>=100 x0.90, tier gold5%/silver2%, tax rate placeholder 0). format_money stub NotImplemented. Next: advance.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))