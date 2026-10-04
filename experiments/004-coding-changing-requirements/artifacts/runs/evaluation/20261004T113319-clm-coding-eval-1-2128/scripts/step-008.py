import json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("from decimal import Decimal, ROUND_HALF_UP","from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN")
s=s.replace("    return x.quantize(Q, rounding=ROUND_HALF_UP)","    return x.quantize(Q, rounding=ROUND_HALF_EVEN)")
s=s.replace("        amt = amt * Decimal('0.95')\n    return _r(amt)","        amt = amt * Decimal('0.95')\n    return amt")
s=s.replace("def _discount_rate(subtotal, customer, lines):\n    return Decimal('0')","def _discount_rate(subtotal, customer, lines):\n    t = (customer or {}).get('tier')\n    return {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}.get(t, Decimal('0'))")
s=s.replace("""    discount = _r(subtotal * _discount_rate(subtotal, customer, lines))
    tax = _r((subtotal - discount) * _tax_rate(customer))
    total = subtotal - discount + tax
    return {'subtotal': str(_r(subtotal)), 'discount': str(discount), 'tax': str(tax), 'total': str(_r(total))}""","""    discount = subtotal * _discount_rate(subtotal, customer, lines)
    tax = (subtotal - discount) * _tax_rate(customer)
    rs, rd, rt = _r(subtotal), _r(discount), _r(tax)
    total = rs - rd + rt
    return {'subtotal': str(rs), 'discount': str(rd), 'tax': str(rt), 'total': str(total)}""")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])
c={'format':'clm-context/v1','entries':[{'id':'sum1','role':'summary','body':'Task: invoice pkg in /task/workspace/invoice/core.py (compute_invoice, format_money stub raises NotImplementedError). Implemented: Decimal; _validate (empty lines, qty positive int, price>=0 -> ValueError); bulk qty>=200 x0.88 elif >=50 x0.95; stage3: tier discount gold 5% silver 2% via _discount_rate(subtotal,customer,lines); tax _tax_rate(customer)=0.10 on exact sub-disc; no line rounding; round sub/disc/tax half-even via _r; total=rs-rd+rt. Edit core.py via str.replace. Stage 3 released; next: check tests, advance.'}]}
json.dump(c,open('/task/workspace/context.json','w'))