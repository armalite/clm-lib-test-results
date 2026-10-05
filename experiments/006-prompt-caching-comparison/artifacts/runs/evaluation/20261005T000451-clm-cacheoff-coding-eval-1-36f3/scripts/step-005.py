p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("""    if line['qty'] >= 100:
        amt = amt * Decimal('0.90')""","""    if line['qty'] >= 200:
        amt = amt * Decimal('0.88')
    elif line['qty'] >= 50:
        amt = amt * Decimal('0.95')""")
s=s.replace("""def compute_invoice(lines, customer):
""","""def validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q = l.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError('bad qty')
        if Decimal(str(l.get('unit_price'))) < 0:
            raise ValueError('negative price')


def compute_invoice(lines, customer):
    validate(lines)
""")
open(p,'w').write(s)
import json
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'invoice/core.py: line_amount (stage2 bulk: qty>=200 x0.88, elif >=50 x0.95; round half up 2dp), validate(lines) ValueError on empty/non-positive-int qty/negative price, discount_rate()=0, tax_rate()=0.10, compute_invoice returns dict of 2dp strings subtotal/discount/tax/total. format_money stub. Stages 1-2 implemented. Tests: unittest discover -s /task/fixtures/current-tests cwd /task/workspace.'}]},open('/task/workspace/context.json','w'))
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])