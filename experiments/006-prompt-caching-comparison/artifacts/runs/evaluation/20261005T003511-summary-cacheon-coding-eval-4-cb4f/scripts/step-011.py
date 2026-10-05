p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("from decimal import Decimal, ROUND_HALF_UP","from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN")
s=s.replace("        amt = amt * Decimal('0.95')\n    return r2(amt)","        amt = amt * Decimal('0.95')\n    return amt")
s=s.replace("q <= 0:","q < 0:")
i=s.index('def compute_invoice');j=s.index('_PREFIX = ')
s=s[:i]+'''def re2(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_EVEN)


def compute_invoice(lines, customer):
    validate(lines)
    sub = sum((line_amount(l) for l in lines if l['qty'] != 0), Decimal('0'))
    disc = sub * tier_rate(customer)
    if customer.get('tax_exempt') is True:
        tax = Decimal('0')
    else:
        tax = (sub - disc) * tax_rate(customer)
    s_, d_, t_ = re2(sub), re2(disc), re2(tax)
    total = s_ - d_ + t_
    return {'subtotal': str(s_), 'discount': str(d_), 'tax': str(t_), 'total': str(re2(total))}


'''+s[j:]
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage4 done.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2500:])