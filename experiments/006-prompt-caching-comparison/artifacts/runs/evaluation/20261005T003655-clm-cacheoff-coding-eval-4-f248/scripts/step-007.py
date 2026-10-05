import json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("        if l['qty']>=100:\n            a*=Decimal('0.90')\n","        if l['qty']>=200:\n            a*=Decimal('0.88')\n        elif l['qty']>=50:\n            a*=Decimal('0.95')\n")
s=s.replace("def format_money(amount, currency):\n    raise NotImplementedError","PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}\n\ndef format_money(amount, currency):\n    if currency not in PFX:\n        raise ValueError('currency')\n    d=_r(Decimal(str(amount)))\n    sign='-' if d<0 else ''\n    return sign+PFX[currency]+str(abs(d))")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'core.py: compute_invoice(lines,customer) _r half-up, bulk qty>=200 x0.88 elif >=50 x0.95 per line, TIER platinum .10 gold .07 silver .03, tax 10% on (sub-disc), validation (empty, qty pos int, price>=0 -> ValueError). format_money PFX NZ$/A$/US$, 2dp, - before prefix, else ValueError. Stage 3 applied; next: check tests then advance to stage 4.'}]},open('/task/workspace/context.json','w'))