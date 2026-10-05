p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("TIER = {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}","TIER = {'platinum': Decimal('0.10'), 'gold': Decimal('0.07'), 'silver': Decimal('0.03')}")
s=s.replace("def tax_rate(lines, customer):\n    return Decimal('0')","def tax_rate(lines, customer):\n    return Decimal('0.10')")
s=s.replace("def compute_invoice(lines, customer):\n","""def validate(lines):
    if not lines:
        raise ValueError('empty')
    for l in lines:
        q = l.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError('qty')
        if Decimal(str(l.get('unit_price'))) < 0:
            raise ValueError('price')

def compute_invoice(lines, customer):
    validate(lines)
""")
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1+2 done in invoice/core.py: r2(), line_amount (bulk qty>=100 x0.90), discount_rate tiers platinum10/gold7/silver3, tax_rate()=0.10, validate(lines) (empty/qty non-positive-int/neg price -> ValueError), compute_invoice returns str dict subtotal/discount/tax/total, format_money stub. Tests: unittest discover -s /task/fixtures/current-tests.'}]},open('/task/workspace/context.json','w'))