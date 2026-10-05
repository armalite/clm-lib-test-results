p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("def tax_rate(customer):\n    return Decimal('0.10')","def tax_rate(customer):\n    return {'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(customer.get('region'),Decimal('0.12'))")
s=s.replace("    tax=(sub-disc)*tax_rate(customer)","    tax=Decimal('0') if customer.get('tax_exempt') is True else (sub-disc)*tax_rate(customer)")
s=s.replace("def format_money(amount, currency):\n    raise NotImplementedError","def format_money(amount, currency):\n    pre={'NZD':'NZ$','AUD':'A$','USD':'US$'}\n    if currency not in pre:\n        raise ValueError('bad currency')\n    a=r2(Decimal(str(amount)))\n    sign='-' if a<0 else ''\n    return sign+pre[currency]+str(abs(a))")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])