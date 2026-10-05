import json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("""    sub=Decimal(0)
    for l in lines:
        a=Decimal(l['qty'])*Decimal(l['unit_price'])
        if l['qty']>=100: a*=Decimal('0.90')
""","""    if not lines: raise ValueError('empty lines')
    sub=Decimal(0)
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<=0: raise ValueError('bad qty')
        up=Decimal(str(l['unit_price']))
        if up<0: raise ValueError('negative price')
        a=Decimal(q)*up
        if q>=200: a*=Decimal('0.88')
        elif q>=50: a*=Decimal('0.95')
""")
open(p,'w').write(s)
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1+2 done in invoice/core.py: compute_invoice (validation ValueError: empty lines, qty not positive int, negative unit_price; bulk qty>=200 x0.88 elif >=50 x0.95; line round half-up; tax 10%; discount 0; returns str dict subtotal/discount/tax/total). format_money unimplemented. Reqs in /task/fixtures/stage-N/REQUIREMENTS.md. Next: advance to stage 3.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])