p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("from decimal import Decimal, ROUND_HALF_UP, InvalidOperation","from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, InvalidOperation")
s=s.replace("""        sub += r2(q * p)
    disc = r2(sub * discount_rate(lines, customer, sub))
    tax = r2((sub - disc) * tax_rate(customer))
    total = sub - disc + tax""","""        amt = q * p
        if q >= 100:
            amt = amt * Decimal('0.90')
        sub += amt
    edisc = sub * discount_rate(lines, customer, sub)
    etax = (sub - edisc) * tax_rate(customer)
    sub = sub.quantize(Q, rounding=ROUND_HALF_EVEN)
    disc = edisc.quantize(Q, rounding=ROUND_HALF_EVEN)
    tax = etax.quantize(Q, rounding=ROUND_HALF_EVEN)
    total = sub - disc + tax""")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage3 done: bulk qty>=100 x0.90; exact calc, half-even round sub/disc/tax\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])