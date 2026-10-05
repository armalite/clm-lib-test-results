p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    tax=(sub-disc)*Decimal('0.10')","    c=customer or {}\n    trate={'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(c.get('region'),Decimal('0.12'))\n    if c.get('tax_exempt') is True: trate=Decimal('0')\n    tax=(sub-disc)*trate")
s=s.replace("def format_money(amount, currency):\n    raise NotImplementedError\n",'''PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in PFX: raise ValueError('bad currency')
    try: a=Decimal(str(amount))
    except InvalidOperation: raise ValueError('bad amount')
    if not a.is_finite(): raise ValueError('bad amount')
    a=r2(a)
    neg=a<0
    body=str(abs(a))
    return ('-' if neg else '')+PFX[currency]+body
''')
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('Stage4 done.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])