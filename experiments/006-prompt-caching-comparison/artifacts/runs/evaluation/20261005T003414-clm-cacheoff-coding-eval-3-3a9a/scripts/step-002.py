import json,subprocess,sys
src='''from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def _r(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)

TAX_RATE=Decimal('0.10')

def _discount_rate(lines, customer, subtotal):
    return Decimal('0')

def _tax_rate(customer):
    return TAX_RATE

def compute_invoice(lines, customer):
    subtotal=sum((_r(Decimal(l['qty'])*Decimal(str(l['unit_price']))) for l in lines), Decimal('0'))
    subtotal=_r(subtotal)
    discount=_r(subtotal*_discount_rate(lines, customer, subtotal))
    tax=_r((subtotal-discount)*_tax_rate(customer))
    total=subtotal-discount+tax
    return {'subtotal':str(subtotal),'discount':str(discount),'tax':str(tax),'total':str(_r(total))}

PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PREFIX: raise ValueError(currency)
    a=_r(Decimal(str(amount)))
    sign='-' if a<0 else ''
    return sign+PREFIX[currency]+str(abs(a))
'''
open('/task/workspace/invoice/core.py','w').write(src)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 done: core.py has _r round, _discount_rate(lines,customer,subtotal)=0, _tax_rate(customer)=0.10, format_money PREFIX dict. Tests run via unittest discover.'}]},open('/task/workspace/context.json','w'))