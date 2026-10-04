import json,subprocess,sys
p='/task/workspace/invoice/core.py';c=open(p).read()
c=c.replace("from decimal import Decimal, ROUND_HALF_UP","from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN")
c=c.replace("def discount_rate(subtotal, customer):\n    return Decimal('0')","def discount_rate(subtotal, customer):\n    t=(customer or {}).get('tier')\n    return {'gold':Decimal('0.05'),'silver':Decimal('0.02')}.get(t,Decimal('0'))")
c=c.replace("    return r2(a)\n","    return a\n")
c=c.replace("""    disc=r2(sub*discount_rate(sub,customer))
    tax=r2((sub-disc)*tax_rate(customer))
    tot=sub-disc+tax
    return {k:str(r2(v))""","""    disc=sub*discount_rate(sub,customer)
    tax=(sub-disc)*tax_rate(customer)
    rs,rd,rt=(Decimal(x).quantize(Q,rounding=ROUND_HALF_EVEN) for x in (sub,disc,tax))
    tot=rs-rd+rt
    sub,disc,tax=rs,rd,rt
    return {k:str(v)""")
open(p,'w').write(c)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2000:])
ctx={'format':'clm-context/v1','entries':[{'id':'sum1','role':'summary','body':"invoice/core.py: Decimal; line_amount unrounded, bulk qty>=200 x0.88, >=50 x0.95; discount_rate tier gold .05 silver .02 else 0; tax .10 on exact (sub-disc); round sub/disc/tax half-even, total=sum of rounded; output dict of str values subtotal/discount/tax/total; validate() ValueError empty/bad qty/neg price. format_money(amount,currency) NotImplemented. Stages 1-3 done (pending test check)."}]}
json.dump(ctx,open('/task/workspace/context.json','w'))