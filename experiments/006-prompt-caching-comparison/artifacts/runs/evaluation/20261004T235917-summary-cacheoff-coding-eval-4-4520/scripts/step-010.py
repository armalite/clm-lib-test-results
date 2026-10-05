p='/task/workspace/invoice/core.py';s=open(p).read()
s=s.replace("    return r2(amt)\n","    return amt\n")
s=s.replace("q <= 0:","q < 0:")
s=s.replace("from decimal import Decimal, ROUND_HALF_UP","from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN\n\ndef re2(x):\n    return x.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)")
i=s.index('def compute_invoice');j=s.index('PREFIX =')
s=s[:i]+'''def compute_invoice(lines, customer):
    validate(lines)
    sub = sum((line_amount(l) for l in lines if l['qty'] != 0), Decimal('0'))
    disc = sub * discount_rate(customer)
    tax = Decimal('0') if customer.get('tax_exempt') is True else (sub - disc) * tax_rate(customer)
    rs, rd, rt = re2(sub), re2(disc), re2(tax)
    total = rs - rd + rt
    return {'subtotal': str(rs), 'discount': str(rd), 'tax': str(rt), 'total': str(re2(total))}

'''+s[j:]
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('Stage4 done.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2500:])