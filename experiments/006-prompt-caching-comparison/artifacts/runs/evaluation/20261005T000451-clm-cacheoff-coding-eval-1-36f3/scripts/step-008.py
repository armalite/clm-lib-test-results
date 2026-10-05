p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("from decimal import Decimal, ROUND_HALF_UP","from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN")
s=s.replace("""        amt = amt * Decimal('0.95')
    return r2(amt)""","""        amt = amt * Decimal('0.95')
    return amt""")
s=s.replace("""def discount_rate(subtotal, lines, customer):
    return Decimal('0')""","""def discount_rate(subtotal, lines, customer):
    tier = (customer or {}).get('tier')
    return {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}.get(tier, Decimal('0'))""")
i=s.index('def compute_invoice'); j=s.index('def format_money')
s=s[:i]+"""def he(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_EVEN)


def compute_invoice(lines, customer):
    validate(lines)
    sub = sum((line_amount(l, customer) for l in lines), Decimal('0'))
    disc = sub * discount_rate(sub, lines, customer)
    tax = (sub - disc) * tax_rate(customer)
    rs, rd, rt = he(sub), he(disc), he(tax)
    total = rs - rd + rt
    return {'subtotal': str(rs), 'discount': str(rd), 'tax': str(rt), 'total': str(total.quantize(Q))}


"""+s[j:]
s=s.replace("Decimal(line['unit_price'])","Decimal(str(line['unit_price']))")
open(p,'w').write(s)
import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[{'id':'n1','role':'note','body':'invoice/core.py: line_amount exact (bulk qty>=200 x0.88, elif >=50 x0.95), validate(lines) ValueError on empty/bad qty/neg price, discount_rate tier gold5% silver2%, tax_rate()=0.10, compute_invoice: exact sums then half-even round sub/disc/tax, total=sum of rounded; returns 2dp strings. format_money stub. Stages 1-3 implemented.'}]
json.dump(c,open('/task/workspace/context.json','w'))
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])