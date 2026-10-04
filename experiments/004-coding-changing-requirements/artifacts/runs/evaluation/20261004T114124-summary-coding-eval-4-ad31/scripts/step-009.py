p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    return r2(amt)","    return amt")
s=s.replace("q <= 0:","q < 0:")
s=s.replace("""    subtotal = sum((line_amount(l) for l in lines), Decimal('0'))
    discount = r2(subtotal * discount_rate(customer))
    tax = r2((subtotal - discount) * tax_rate(customer))
    total = subtotal - discount + tax""","""    from decimal import ROUND_HALF_EVEN
    he = lambda x: x.quantize(Q, rounding=ROUND_HALF_EVEN)
    ex = sum((line_amount(l) for l in lines if l['qty'] != 0), Decimal('0'))
    dex = ex * discount_rate(customer)
    tex = Decimal('0') if customer.get('tax_exempt') is True else (ex - dex) * tax_rate(customer)
    subtotal, discount, tax = he(ex), he(dex), he(tex)
    total = subtotal - discount + tax""")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('Stage4 done.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])