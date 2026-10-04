import re,json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("""    amt=Decimal(int(line['qty']))*Decimal(str(line['unit_price']))
    if int(line['qty'])>=100:
        amt*=Decimal('0.90')""","""    q=line['qty']
    amt=Decimal(q)*Decimal(str(line['unit_price']))
    if q>=200:
        amt*=Decimal('0.88')
    elif q>=50:
        amt*=Decimal('0.95')""")
s=s.replace("""def compute_invoice(lines, customer):
""","""def validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError('bad qty')
        try:
            pr=Decimal(str(l.get('unit_price')))
        except Exception:
            raise ValueError('bad price')
        if not pr.is_finite() or pr<0:
            raise ValueError('negative price')

def compute_invoice(lines, customer):
    validate(lines)
""")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
c={'format':'clm-context/v1','entries':[{'id':'sum1','role':'summary','body':'invoice/core.py implements: r2 half-up, line_amount (bulk >=200 x0.88, >=50 x0.95), discount_rate()=0 hook (lines,customer,subtotal), tax_rate(customer)=0.10, validate() (empty lines, qty positive int, price>=0 -> ValueError), compute_invoice returns 2dp strings. format_money(amount,currency) still NotImplementedError. Stages 1-2 done; next: advance to stage 3.'}]}
json.dump(c,open('/task/workspace/context.json','w'))