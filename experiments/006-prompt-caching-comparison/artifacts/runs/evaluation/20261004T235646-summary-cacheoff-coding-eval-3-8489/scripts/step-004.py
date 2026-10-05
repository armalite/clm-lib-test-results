code='''from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
Q=Decimal('0.01')
def _r(x, m=ROUND_HALF_EVEN): return x.quantize(Q, rounding=m)

TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}
def _discount_rate(lines, customer, subtotal):
    return TIER.get(customer.get('tier'), Decimal('0'))

def _tax_rate(customer):
    if customer.get('tax_exempt') is True: return Decimal('0')
    return Decimal('0.10')

def compute_invoice(lines, customer):
    sub=sum((int(l['qty'])*Decimal(str(l['unit_price'])) for l in lines), Decimal('0'))
    disc=sub*_discount_rate(lines, customer, sub)
    tax=(sub-disc)*_tax_rate(customer)
    s,d,t=_r(sub),_r(disc),_r(tax)
    total=s-d+t
    return {k:str(_r(v)) for k,v in dict(subtotal=s,discount=d,tax=t,total=total).items()}

PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in PREFIX: raise ValueError(currency)
    a=_r(Decimal(str(amount)), ROUND_HALF_UP)
    s='-' if a<0 else ''
    return f"{s}{PREFIX[currency]}{abs(a)}"
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/NOTES.md','a').write('Stage2 done: tier gold5/silver2, tax_exempt, half-even rounding of exact totals.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2000:])