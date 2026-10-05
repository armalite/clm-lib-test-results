import json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("        if l['qty']>=100: a*=Decimal('0.90')\n","        if l['qty']>=200: a*=Decimal('0.88')\n        elif l['qty']>=50: a*=Decimal('0.95')\n")
s=s.replace("def format_money(amount, currency):\n    raise NotImplementedError","""PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}\n\ndef format_money(amount, currency):\n    if currency not in PFX: raise ValueError('currency')\n    d=r2(Decimal(str(amount)))\n    sign='-' if d<0 else ''\n    return sign+PFX[currency]+str(abs(d))""")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stages1-3 implemented in invoice/core.py: compute_invoice(lines,customer) returns str dict subtotal/discount/tax/total; line round half-up; bulk qty>=200 x0.88 elif >=50 x0.95; tiers platinum10/gold7/silver3%; tax 10% on (sub-disc); ValueError on empty lines, non-positive-int qty, negative price. format_money(amount,currency) NZ$/A$/US$ prefixes, 2dp, -prefix for negative, else ValueError (dict PFX). Next: advance if tests OK.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))