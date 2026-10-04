import re,json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("""    amt = Decimal(int(line['qty'])) * Decimal(str(line['unit_price']))
    if int(line['qty']) >= 100:
        amt = amt * Decimal('0.90')""","""    q = line['qty']
    amt = Decimal(q) * Decimal(str(line['unit_price']))
    if q >= 200:
        amt = amt * Decimal('0.88')
    elif q >= 50:
        amt = amt * Decimal('0.95')""")
s=s.replace("""def compute_invoice(lines, customer):
""","""def _validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q = l.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError('bad qty')
        try:
            p = Decimal(str(l.get('unit_price')))
        except Exception:
            raise ValueError('bad price')
        if not p.is_finite() or p < 0:
            raise ValueError('negative price')


def compute_invoice(lines, customer):
    _validate(lines)
""")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
c={'format':'clm-context/v1','entries':[{'id':'sum1','role':'summary','body':'Task: invoice pkg in /task/workspace/invoice/core.py (compute_invoice, format_money stub raises NotImplementedError). Implemented: Decimal, line round half-up 2dp, discount via _discount_rate(subtotal,customer,lines)=0, tax via _tax_rate(customer)=0.10, total=sub-disc+tax; stage2: _validate (empty lines, qty positive int, price>=0 -> ValueError), bulk qty>=200 x0.88 elif >=50 x0.95. Edit core.py via str.replace. Stage 2 released; next: run tests then advance.'}]}
json.dump(c,open('/task/workspace/context.json','w'))