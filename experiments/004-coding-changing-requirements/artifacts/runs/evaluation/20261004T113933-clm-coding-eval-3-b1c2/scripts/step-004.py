code='''from decimal import Decimal, ROUND_HALF_EVEN

Q=Decimal('0.01')

def r2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_EVEN)

def discount_rate(lines, customer, subtotal):
    return {'gold':Decimal('0.05'),'silver':Decimal('0.02')}.get(customer.get('tier'),Decimal('0'))

def tax_rate(customer):
    return Decimal('0.10')

def compute_invoice(lines, customer):
    sub=sum((Decimal(str(l['qty']))*Decimal(str(l['unit_price'])) for l in lines), Decimal('0'))
    disc=sub*discount_rate(lines, customer, sub)
    tax=Decimal('0') if customer.get('tax_exempt') is True else (sub-disc)*tax_rate(customer)
    s,d,t=r2(sub),r2(disc),r2(tax)
    return {'subtotal':str(s),'discount':str(d),'tax':str(t),'total':str(s-d+t)}

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
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'invoice/core.py: stage1+2 done. exact sums, half-even round of sub/disc/tax, total=s-d+t; discount_rate hook tier gold5/silver2; tax_exempt True->0; tax_rate hook 0.10; format_money NZ$/A$/US$, neg -prefix, else ValueError (format uses r2 half-even now).'}]},open('/task/workspace/context.json','w'))