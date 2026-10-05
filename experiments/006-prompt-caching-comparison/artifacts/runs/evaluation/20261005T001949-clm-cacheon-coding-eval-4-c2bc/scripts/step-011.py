p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("from decimal import Decimal, ROUND_HALF_UP","from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN")
s=s.replace("        a = a * Decimal('0.95')\n    return r2(a)","        a = a * Decimal('0.95')\n    return a")
s=s.replace("q <= 0","q < 0")
i=s.index('def compute_invoice');j=s.index('PREFIX =')
s=s[:i]+'''def re2(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def compute_invoice(lines, customer):
    validate(lines)
    act = [l for l in lines if l['qty'] != 0]
    sub = sum((line_amount(l) for l in act), Decimal('0'))
    disc = sub * discount_rate(act, customer, sub)
    if customer.get('tax_exempt') is True:
        tax = Decimal('0')
    else:
        tax = (sub - disc) * tax_rate(act, customer)
    sub, disc, tax = re2(sub), re2(disc), re2(tax)
    total = sub - disc + tax
    return {k: str(re2(v)) for k, v in (('subtotal', sub), ('discount', disc), ('tax', tax), ('total', total))}

'''+s[j:]
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'All 4 stages released. Stage4 applied in invoice/core.py: no line rounding, half-even rounding of sub/disc/tax, tax_exempt, qty 0 skipped. Check test result then final.'}]},open('/task/workspace/context.json','w'))