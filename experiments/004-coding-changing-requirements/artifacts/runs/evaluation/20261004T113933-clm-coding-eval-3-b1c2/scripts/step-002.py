code='''from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def r2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)

def discount_rate(lines, customer, subtotal):
    return Decimal('0')

def tax_rate(customer):
    return Decimal('0.10')

def compute_invoice(lines, customer):
    subtotal=sum((r2(Decimal(l['qty'])*Decimal(str(l['unit_price']))) for l in lines), Decimal('0'))
    subtotal=r2(subtotal)
    discount=r2(subtotal*discount_rate(lines, customer, subtotal))
    tax=r2((subtotal-discount)*tax_rate(customer))
    total=subtotal-discount+tax
    return {'subtotal':str(subtotal),'discount':str(discount),'tax':str(tax),'total':str(r2(total))}

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
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 done in invoice/core.py: r2 half-up per line, discount_rate()=0 hook, tax_rate()=0.10 hook, format_money NZ$/A$/US$, neg -prefix, else ValueError.'}]},open('/task/workspace/context.json','w'))