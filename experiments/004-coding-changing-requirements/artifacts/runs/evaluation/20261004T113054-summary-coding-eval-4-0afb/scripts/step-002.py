import subprocess,sys
open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice\n')
open('/task/workspace/invoice/core.py','w').write('''from decimal import Decimal, ROUND_HALF_UP
Q=Decimal('0.01')
def r(x): return x.quantize(Q, rounding=ROUND_HALF_UP)
TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}
def tax_rate(customer, sub):
    return Decimal(0)
def compute_invoice(lines, customer):
    sub=Decimal(0)
    for l in lines:
        a=Decimal(l['qty'])*Decimal(str(l['unit_price']))
        if l['qty']>=100: a*=Decimal('0.90')
        sub+=r(a)
    disc=r(sub*TIER.get(customer.get('tier'),Decimal(0)))
    tax=r((sub-disc)*tax_rate(customer, sub))
    tot=sub-disc+tax
    return {k:str(r(v)) for k,v in dict(subtotal=sub,discount=disc,tax=tax,total=tot).items()}
''')
open('/task/workspace/NOTES.md','w').write('stage1 done: core.py rounding/bulk/tier\n')
p=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(p.stderr[-1500:])