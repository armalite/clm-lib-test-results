open('/task/workspace/invoice/core.py','w').write('''from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
def r2(x): return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)
TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}
def validate(lines):
    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')
        if Decimal(str(l['unit_price']))<0: raise ValueError('price')
def compute_invoice(lines, customer):
    validate(lines)
    amts=[r2(l['qty']*Decimal(str(l['unit_price']))) for l in lines]
    sub=sum(amts,Decimal(0))
    disc=r2(TIER.get(customer.get('tier'),Decimal(0))*sub)
    ship=Decimal('7.50') if sub-disc<Decimal('100') else Decimal(0)
    tax=r2((sub-disc)*0)
    tot=sub-disc+ship+tax
    return {k:str(r2(v)) for k,v in dict(subtotal=sub,discount=disc,shipping=ship,tax=tax,total=tot).items()}
''')
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stages 1-2 implemented in invoice/core.py (r2 half-up helper, TIER dict, validate(), shipping 7.50 if sub-disc<100, tax rate 0 placeholder). Rules: round line amounts, discount components, tax to 2dp as computed; tier gold 5% silver 2% of tier-eligible amount (=subtotal default); ValueError on empty lines, qty not int>0, negative price; shipping not taxed/discounted.'}]}
json.dump(c,open('/task/workspace/context.json','w'))