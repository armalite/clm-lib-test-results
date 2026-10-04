code='''from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')
def r2(x): return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)

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
    return {k:str(r2(v)) for k,v in [('subtotal',subtotal),('discount',discount),('tax',tax),('total',total)]}

PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in PREFIX: raise ValueError(currency)
    a=r2(Decimal(str(amount)))
    sign='-' if a<0 else ''
    return sign+PREFIX[currency]+str(abs(a))
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/NOTES.md','w').write('Stage1 done: rounding half-up per line, tax 10%, format_money NZ$/A$/US$.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])