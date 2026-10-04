import subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    tax=(sub-disc)*Decimal('0.10')","    tr=REGION.get(customer.get('region'),Decimal('0.12'))\n    if customer.get('tax_exempt') is True: tr=Decimal('0')\n    tax=(sub-disc)*tr")
s+='''
REGION={'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}
PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in PREFIX: raise ValueError('bad currency')
    a=r2(Decimal(str(amount)))
    sign='-' if a<0 else ''
    return sign+PREFIX[currency]+str(abs(a))
'''
open(p,'w').write(s)
open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice, format_money\n')
open('/task/workspace/NOTES.md','a').write('\nS4: region tax, tax_exempt, format_money done.\n')
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])