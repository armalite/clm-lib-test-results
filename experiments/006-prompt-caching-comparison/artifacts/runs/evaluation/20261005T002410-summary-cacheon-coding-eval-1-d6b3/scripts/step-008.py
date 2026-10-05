p='/task/workspace/invoice/core.py';s=open(p).read()
s=s.replace("tax=(subtotal-discount)*Decimal('0.10')","trate={'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(customer.get('region'),Decimal('0.12'))\n    if customer.get('tax_exempt') is True:\n        trate=Decimal('0')\n    tax=(subtotal-discount)*trate")
s=s.replace("def format_money(amount, currency):\n    raise NotImplementedError","def format_money(amount, currency):\n    pre={'NZD':'NZ$','AUD':'A$','USD':'US$'}\n    if currency not in pre:\n        raise ValueError('bad currency')\n    a=r2(Decimal(str(amount)))\n    sign='-' if a<0 else ''\n    return sign+pre[currency]+str(abs(a))")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('Stage4: region tax, exempt, format_money.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])