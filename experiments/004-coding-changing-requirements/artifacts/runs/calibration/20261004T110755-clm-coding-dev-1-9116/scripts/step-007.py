p='/task/workspace/invoice/core.py'
s=open(p).read()
i=s.index('def compute_invoice');j=s.index('def format_money')
new='''from decimal import ROUND_HALF_EVEN
def _re(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)

def _line(l):
    a=l['qty']*Decimal(str(l['unit_price']))
    if l['qty']>=100:
        a=a*Decimal('0.90')
    return a

def compute_invoice(lines, customer):
    _validate(lines)
    sub=sum((_line(l) for l in lines), Decimal('0'))
    disc=sub*discount_rate(lines,customer,sub)
    tax=(sub-disc)*tax_rate(customer)
    rs,rd,rt=_re(sub),_re(disc),_re(tax)
    total=rs-rd+rt
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(total)}

'''
s=s[:i]+new+s[j:]
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'summary','body':'invoice/core.py: _r (half up, unused now), _re half-even, _validate, _line (qty>=100 x0.90), discount_rate(lines,customer,subtotal) tier gold5%/silver2%, tax_rate(customer) NZ15 AU10 US0 else12, compute_invoice (stage3: exact sums, round sub/disc/tax half-even, total=sum of rounded), format_money (NotImplemented). Stages 1-3 implemented; check test result of step 7 then advance to stage 4.'}]}
json.dump(c,open('/task/workspace/context.json','w'))