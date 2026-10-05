import json,subprocess,sys
src='''from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def r2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)

def discount_rate(lines, customer, subtotal):
    return Decimal('0')

def tax_rate(customer):
    return Decimal('0.10')

def compute_invoice(lines, customer):
    subtotal=sum((r2(Decimal(l['qty'])*Decimal(l['unit_price'])) for l in lines), Decimal('0'))
    subtotal=r2(subtotal)
    disc=r2(subtotal*discount_rate(lines,customer,subtotal))
    tax=r2((subtotal-disc)*tax_rate(customer))
    total=subtotal-disc+tax
    return {k:str(r2(v)) for k,v in (('subtotal',subtotal),('discount',disc),('tax',tax),('total',total))}

PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError(currency)
    a=r2(Decimal(amount))
    s='-' if a<0 else ''
    return s+PREFIX[currency]+str(abs(a))
'''
open('/task/workspace/invoice/core.py','w').write(src)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 done: invoice/core.py has r2 (half-up), discount_rate(lines,customer,subtotal)=0, tax_rate(customer)=0.10, compute_invoice, format_money (NZ$/A$/US$, -prefix, ValueError). Tests run via unittest discover.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))