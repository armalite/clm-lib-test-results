import json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("from decimal import Decimal, ROUND_HALF_UP","from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN")
s=s.replace("""def discount_rate(lines, customer, subtotal):
    return Decimal('0')""","""def discount_rate(lines, customer, subtotal):
    t=(customer or {}).get('tier')
    return {'gold':Decimal('0.05'),'silver':Decimal('0.02')}.get(t,Decimal('0'))

def r2e(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)""")
s=s.replace("    return r2(amt)\n","    return amt\n")
s=s.replace("""    discount=r2(subtotal*discount_rate(lines,customer,subtotal))
    tax=r2((subtotal-discount)*tax_rate(customer))
    total=subtotal-discount+tax
    return {k:str(r2(v))""","""    discount=subtotal*discount_rate(lines,customer,subtotal)
    tax=(subtotal-discount)*tax_rate(customer)
    subtotal,discount,tax=r2e(subtotal),r2e(discount),r2e(tax)
    total=subtotal-discount+tax
    return {k:str(r2e(v))""")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])
c={'format':'clm-context/v1','entries':[{'id':'sum1','role':'summary','body':'invoice/core.py implements: line_amount unrounded (bulk >=200 x0.88, >=50 x0.95), discount_rate(lines,customer,subtotal) tier gold 5%/silver 2%, tax_rate(customer)=0.10, exact calc then r2e half-even on subtotal/discount/tax, total from rounded; validate() (empty lines, qty positive int, price>=0 -> ValueError); returns 2dp strings. format_money(amount,currency) still NotImplementedError. Stages 1-3 implemented (check test result in last obs); next: advance to stage 4.'}]}
json.dump(c,open('/task/workspace/context.json','w'))