import re,json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("""    amt = Decimal(int(line['qty'])) * Decimal(str(line['unit_price']))
    if int(line['qty']) >= 100:
        amt = amt * Decimal('0.90')""","""    q = int(line['qty'])
    amt = Decimal(q) * Decimal(str(line['unit_price']))
    if q >= 200:
        amt = amt * Decimal('0.88')
    elif q >= 50:
        amt = amt * Decimal('0.95')""")
s=s.replace("""def compute_invoice(lines, customer):
""","""def validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q = l.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError('bad qty')
        try:
            up = Decimal(str(l['unit_price']))
        except Exception:
            raise ValueError('bad price')
        if not up.is_finite() or up < 0:
            raise ValueError('negative price')


def compute_invoice(lines, customer):
    validate(lines)
""")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
c={'format':'clm-context/v1','entries':[{'id':'sum1','role':'summary','body':'Stages 1-2 implemented in /task/workspace/invoice/core.py: funcs r2, discount_rate(lines,customer,subtotal)->0, tax_rate(customer)->0.10, line_amount (bulk qty>=200 x0.88, >=50 x0.95, then round), validate(lines) (ValueError empty/qty not positive int/neg price), compute_invoice. format_money(amount,currency) still NotImplemented (exported in __init__). Run tests via unittest discover -s /task/fixtures/current-tests cwd /task/workspace.'}]}
json.dump(c,open('/task/workspace/context.json','w'))