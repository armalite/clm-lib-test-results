import json,subprocess,sys
src='''from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Q=Decimal('0.01')

def r2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_UP)

def be2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_EVEN)

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}

def discount_rate(lines, customer, subtotal):
    return TIER.get((customer or {}).get('tier'), Decimal('0'))

def tax_rate(customer):
    return Decimal('0.10')

def compute_invoice(lines, customer):
    customer=customer or {}
    sub=sum((Decimal(str(l['qty']))*Decimal(str(l['unit_price'])) for l in lines), Decimal('0'))
    disc=sub*discount_rate(lines,customer,sub)
    tax=Decimal('0') if customer.get('tax_exempt') is True else (sub-disc)*tax_rate(customer)
    s,d,t=be2(sub),be2(disc),be2(tax)
    return {'subtotal':str(s),'discount':str(d),'tax':str(t),'total':str(s-d+t)}

PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError(currency)
    a=r2(Decimal(str(amount)))
    s='-' if a<0 else ''
    return s+PREFIX[currency]+str(abs(a))
'''
open('/task/workspace/invoice/core.py','w').write(src)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1+2 in invoice/core.py: format_money (NZ$/A$/US$, -prefix, half-up 2dp, ValueError unknown). Stage2: tier discount gold 5%/silver 2%/else 0 (discount_rate(lines,customer,subtotal)); tax_rate(customer)=0.10; tax_exempt is True -> tax 0; CHANGED rounding: exact sums, round subtotal/discount/tax half-even, total=sum of rounded. compute_invoice returns dict of str subtotal,discount,tax,total.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))