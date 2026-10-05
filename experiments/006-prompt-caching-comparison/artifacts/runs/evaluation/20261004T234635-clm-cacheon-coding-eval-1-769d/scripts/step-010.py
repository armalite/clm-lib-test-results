import json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    t=(sub-d)*Decimal('0.10')\n","    c=customer or {}\n    tr={'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal(0)}.get(c.get('region'),Decimal('0.12'))\n    if c.get('tax_exempt') is True: tr=Decimal(0)\n    t=(sub-d)*tr\n")
s=s.replace("def format_money(amount, currency):\n    raise NotImplementedError","def format_money(amount, currency):\n    pre={'NZD':'NZ$','AUD':'A$','USD':'US$'}\n    if currency not in pre: raise ValueError('bad currency')\n    a=r2(Decimal(str(amount)))\n    neg=a<0\n    return ('-' if neg else '')+pre[currency]+str(abs(a))")
open(p,'w').write(s)
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'All 4 stages released. Stage4 implemented in invoice/core.py: region tax NZ15 AU10 US0 else12, tax_exempt True->0, format_money NZ$/A$/US$, 2dp, -prefix, ValueError other. Next: if tests pass, final.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
sys.path.insert(0,'/task/workspace');import invoice;print(invoice.format_money('-5','NZD'))