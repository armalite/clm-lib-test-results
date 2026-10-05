import json,subprocess,sys
src='''from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q=Decimal('0.01')

def _r(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_EVEN)

TAX_RATE=Decimal('0.10')
TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def _discount_rate(lines, customer, subtotal):
    return TIER.get(customer.get('tier'), Decimal('0'))

def _tax_rate(customer):
    if customer.get('tax_exempt') is True: return Decimal('0')
    return TAX_RATE

def compute_invoice(lines, customer):
    sub=sum((Decimal(str(l['qty']))*Decimal(str(l['unit_price'])) for l in lines), Decimal('0'))
    disc=sub*_discount_rate(lines, customer, sub)
    tax=(sub-disc)*_tax_rate(customer)
    s,d,t=_r(sub),_r(disc),_r(tax)
    return {'subtotal':str(s),'discount':str(d),'tax':str(t),'total':str(_r(s-d+t))}

PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PREFIX: raise ValueError(currency)
    a=Decimal(str(amount)).quantize(Q, rounding=ROUND_HALF_UP)
    sign='-' if a<0 else ''
    return sign+PREFIX[currency]+str(abs(a))
'''
open('/task/workspace/invoice/core.py','w').write(src)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1+2 in core.py: compute_invoice exact then HALF_EVEN round s/d/t; tier gold5 silver2; tax_exempt True->0; tax 10%; format_money PREFIX NZ$/A$/US$ HALF_UP, ValueError unknown. Next: advance.'}]},open('/task/workspace/context.json','w'))