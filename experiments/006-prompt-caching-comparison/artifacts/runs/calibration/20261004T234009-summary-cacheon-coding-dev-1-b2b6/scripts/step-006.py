p='/task/workspace/invoice/core.py'
s=open(p).read()
old=s[s.index('def compute_invoice'):s.index('def format_money')]
new='''def compute_invoice(lines, customer):
    _validate(lines)
    def amt(l):
        a=l['qty']*Decimal(str(l['unit_price']))
        if l['qty']>=100: a=a*Decimal('0.90')
        return a
    sub=sum((amt(l) for l in lines), Decimal('0'))
    disc=sub*discount_rate(lines,customer,sub)
    tax=(sub-disc)*tax_rate(customer)
    E=ROUND_HALF_EVEN
    rs,rd,rt=(x.quantize(Q,rounding=E) for x in (sub,disc,tax))
    total=rs-rd+rt
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(total.quantize(Q))}

'''
s=s.replace(old,new).replace('ROUND_HALF_UP','ROUND_HALF_UP, ROUND_HALF_EVEN',1)
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage3 done: bulk qty>=100 x0.9; no line rounding, half-even on sub/disc/tax.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])