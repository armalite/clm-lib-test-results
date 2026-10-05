code='''from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
def r2(x):return Decimal(x).quantize(Q,rounding=ROUND_HALF_UP)
TAX_RATE=Decimal('0.10')
def discount_rate(lines,customer,subtotal):return Decimal(0)
def tax_rate(customer):return TAX_RATE
def compute_invoice(lines,customer):
    sub=sum((r2(int(l['qty'])*Decimal(str(l['unit_price']))) for l in lines),Decimal(0))
    sub=r2(sub)
    disc=r2(sub*discount_rate(lines,customer,sub))
    tax=r2((sub-disc)*tax_rate(customer))
    tot=sub-disc+tax
    return {k:str(r2(v)) for k,v in (('subtotal',sub),('discount',disc),('tax',tax),('total',tot))}
PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount,currency):
    if currency not in PREFIX: raise ValueError(currency)
    a=r2(Decimal(str(amount)))
    s='-' if a<0 else ''
    return s+PREFIX[currency]+str(abs(a))
'''
open('/task/workspace/invoice/core.py','w').write(code)
open('/task/workspace/NOTES.md','w').write('Stage1 done: half-up line rounding, tax 10%, format_money NZD/AUD/USD, neg sign before prefix.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])