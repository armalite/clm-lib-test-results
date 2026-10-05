import json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("        if l['qty']>=100: a*=Decimal('0.90')\n","        if l['qty']>=200: a*=Decimal('0.88')\n        elif l['qty']>=50: a*=Decimal('0.95')\n")
s=s.replace("def format_money(amount, currency):\n    raise NotImplementedError","PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}\n\ndef format_money(amount, currency):\n    if currency not in PFX: raise ValueError('currency')\n    d=r2(Decimal(str(amount)))\n    sign='-' if d<0 else ''\n    return sign+PFX[currency]+str(abs(d))")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'invoice/core.py: r2 half-up line rounding, bulk qty>=200 x0.88 elif >=50 x0.95, tier platinum10/gold7/silver3%, tax 10% on (sub-disc), validation (empty lines, qty positive int, price>=0 -> ValueError). format_money PFX dict NZ$/A$/US$, -prefix sign, 2dp, else ValueError. Stages 1-3 implemented (step 6).'}]},open('/task/workspace/context.json','w'))