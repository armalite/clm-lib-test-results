p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    tax=(sub-disc)*Decimal('0.10')","    c=customer if isinstance(customer,dict) else {}\n    tr={'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal(0)}.get(c.get('region'),Decimal('0.12'))\n    if c.get('tax_exempt') is True: tr=Decimal(0)\n    tax=(sub-disc)*tr")
s=s.replace("def format_money(amount, currency):\n    raise NotImplementedError","def format_money(amount, currency):\n    pre={'NZD':'NZ$','AUD':'A$','USD':'US$'}\n    if currency not in pre: raise ValueError('currency')\n    a=r2(Decimal(str(amount)))\n    neg=a<0\n    return ('-' if neg else '')+pre[currency]+str(abs(a))")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2000:])