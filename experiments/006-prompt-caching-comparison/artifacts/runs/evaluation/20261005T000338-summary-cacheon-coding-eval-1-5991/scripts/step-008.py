p='/task/workspace/invoice/core.py'
c=open(p).read()
c=c.replace("    tax=(subtotal-discount)*Decimal('0.10')","    cust=customer or {}\n    rate=TAX.get(cust.get('region'),Decimal('0.12'))\n    if cust.get('tax_exempt') is True: rate=Decimal('0')\n    tax=(subtotal-discount)*rate")
c=c.replace("DISC={","TAX={'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}\nDISC={")
c=c.replace("def format_money(amount, currency):\n    raise NotImplementedError","""PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in PFX: raise ValueError('bad currency')
    try: a=Decimal(str(amount))
    except Exception: raise ValueError('bad amount')
    if not a.is_finite(): raise ValueError('bad amount')
    a=r2(a)
    neg=a<0
    s=PFX[currency]+str(abs(a))
    return '-'+s if neg else s""")
open(p,'w').write(c)
open('/task/workspace/NOTES.md','a').write('Stage4: region tax NZ15 AU10 US0 else12; tax_exempt True->0; format_money.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])