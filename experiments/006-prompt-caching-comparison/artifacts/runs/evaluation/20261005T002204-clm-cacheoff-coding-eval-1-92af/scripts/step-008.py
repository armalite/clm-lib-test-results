import json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace('ROUND_HALF_UP','ROUND_HALF_EVEN')
s=s.replace("""def discount_rate(lines, customer, subtotal):
    return Decimal('0')""","""def discount_rate(lines, customer, subtotal):
    t = (customer or {}).get('tier')
    return {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}.get(t, Decimal('0'))""")
s=s.replace("    return r2(amt)\n","    return amt\n")
s=s.replace("""    discount = r2(subtotal * discount_rate(lines, customer, subtotal))
    tax = r2((subtotal - discount) * tax_rate(customer))
    total = subtotal - discount + tax""","""    disc = subtotal * discount_rate(lines, customer, subtotal)
    tax = (subtotal - disc) * tax_rate(customer)
    subtotal, discount, tax = r2(subtotal), r2(disc), r2(tax)
    total = subtotal - discount + tax""")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
c={'format':'clm-context/v1','entries':[{'id':'sum1','role':'summary','body':'Stages 1-3 implemented in /task/workspace/invoice/core.py: r2 (HALF_EVEN), discount_rate(lines,customer,subtotal) tier gold .05 silver .02, tax_rate(customer)->0.10, line_amount (bulk qty>=200 x0.88, >=50 x0.95, unrounded), validate(lines), compute_invoice (exact then round subtotal/discount/tax, total=sum of rounded). format_money(amount,currency) still NotImplemented. Tests: unittest discover -s /task/fixtures/current-tests cwd /task/workspace.'}]}
json.dump(c,open('/task/workspace/context.json','w'))