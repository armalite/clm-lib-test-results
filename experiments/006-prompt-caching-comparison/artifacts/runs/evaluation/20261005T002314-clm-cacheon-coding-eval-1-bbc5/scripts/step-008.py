import json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    tax=(sub-disc)*Decimal('0.10')","    c=customer if isinstance(customer,dict) else {}\n    rate={'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal(0)}.get(c.get('region'),Decimal('0.12'))\n    if c.get('tax_exempt') is True: rate=Decimal(0)\n    tax=(sub-disc)*rate")
s=s.replace("def format_money(amount, currency):\n    raise NotImplementedError","def format_money(amount, currency):\n    pre={'NZD':'NZ$','AUD':'A$','USD':'US$'}\n    if currency not in pre: raise ValueError('currency')\n    a=r2(Decimal(str(amount)))\n    sign='-' if a<0 else ''\n    return sign+pre[currency]+str(abs(a))")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2500:])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','s7.obs')]
json.dump(c,open('/task/workspace/context.json','w'))