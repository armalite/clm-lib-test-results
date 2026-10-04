import re,json
p='/task/workspace/invoice/core.py';c=open(p).read()
c=c.replace("    if int(l['qty'])>=100: a*=Decimal('0.90')\n","    q=int(l['qty'])\n    if q>=200: a*=Decimal('0.88')\n    elif q>=50: a*=Decimal('0.95')\n")
c=c.replace("def compute_invoice(lines, customer):\n","""def validate(lines):
    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')
        try: up=Decimal(str(l['unit_price']))
        except Exception: raise ValueError('price')
        if up<0: raise ValueError('price')

def compute_invoice(lines, customer):
    validate(lines)
""")
open(p,'w').write(c)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
ctx={'format':'clm-context/v1','entries':[{'id':'sum1','role':'summary','body':'invoice/core.py implements: Decimal, r2 half-up rounding per line/discount/tax; tax_rate(customer)=0.10; discount_rate(sub,customer)=0; line_amount bulk: qty>=200 x0.88, >=50 x0.95; validate(lines) ValueError on empty/non-positive-int qty/negative price. format_money(amount,currency) still NotImplemented. Stages 1-2 done; tests run via unittest discover -s /task/fixtures/current-tests.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))