code='''"""Invoice core."""
from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def r2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)

def tax_rate(customer):
    return Decimal('0.10')

def discount_rate(customer, subtotal):
    return Decimal('0')

def compute_invoice(lines, customer):
    subtotal=sum((r2(Decimal(l['qty'])*Decimal(str(l['unit_price']))) for l in lines), Decimal('0.00'))
    subtotal=r2(subtotal)
    discount=r2(subtotal*discount_rate(customer, subtotal))
    tax=r2((subtotal-discount)*tax_rate(customer))
    total=subtotal-discount+tax
    return {k:str(r2(v)) for k,v in [('subtotal',subtotal),('discount',discount),('tax',tax),('total',total)]}

PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError(currency)
    a=r2(Decimal(str(amount)))
    s='-' if a<0 else ''
    return s+PREFIX[currency]+str(abs(a))
'''
open('/task/workspace/invoice/core.py','w').write(code)
import subprocess,sys,json
p=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(p.stderr[-2500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 implemented in invoice/core.py: r2 half-up, tax_rate(customer)=0.10, discount_rate(customer,subtotal)=0, format_money with PREFIX NZ$/A$/US$, ValueError otherwise, -prefix for negatives.'}]},open('/task/workspace/context.json','w'))