code='''from decimal import Decimal, ROUND_HALF_UP

Q=Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def discount_rate(lines, customer, subtotal):
    return Decimal('0')

def tax_rate(customer):
    return Decimal('0.10')

def line_amount(line):
    amt=Decimal(int(line['qty']))*Decimal(str(line['unit_price']))
    if int(line['qty'])>=100:
        amt*=Decimal('0.90')
    return r2(amt)

def compute_invoice(lines, customer):
    subtotal=sum((line_amount(l) for l in lines), Decimal('0'))
    discount=r2(subtotal*discount_rate(lines,customer,subtotal))
    tax=r2((subtotal-discount)*tax_rate(customer))
    total=subtotal-discount+tax
    return {k:str(r2(v)) for k,v in dict(subtotal=subtotal,discount=discount,tax=tax,total=total).items()}


def format_money(amount, currency):
    raise NotImplementedError
'''
open('/task/workspace/invoice/core.py','w').write(code)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])