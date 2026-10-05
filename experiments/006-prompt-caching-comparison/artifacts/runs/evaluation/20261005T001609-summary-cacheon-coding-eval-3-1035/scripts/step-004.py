code='''from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
Q=Decimal('0.01')
def r2(x,m=ROUND_HALF_UP):return Decimal(x).quantize(Q,rounding=m)
def re(x):return r2(x,ROUND_HALF_EVEN)
TAX_RATE=Decimal('0.10')
TIERS={'gold':Decimal('0.05'),'silver':Decimal('0.02')}
def discount_rate(lines,customer,subtotal):return TIERS.get(customer.get('tier'),Decimal(0))
def tax_rate(customer):
    if customer.get('tax_exempt') is True:return Decimal(0)
    return TAX_RATE
def compute_invoice(lines,customer):
    sub=sum((int(l['qty'])*Decimal(str(l['unit_price'])) for l in lines),Decimal(0))
    disc=sub*discount_rate(lines,customer,sub)
    tax=(sub-disc)*tax_rate(customer)
    rs,rd,rt=re(sub),re(disc),re(tax)
    tot=rs-rd+rt
    return {k:str(r2(v)) for k,v in (('subtotal',rs),('discount',rd),('tax',rt),('total',tot))}
PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount,currency):
    if currency not in PREFIX: raise ValueError(currency)
    a=r2(Decimal(str(amount)))
    s='-' if a<0 else ''
    return s+PREFIX[currency]+str(abs(a))
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/NOTES.md','a').write('Stage2 done: tiers gold5 silver2, tax_exempt, half-even rounding of exact sub/disc/tax.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])