p='/task/workspace/invoice/core.py'
c=open(p).read()
i=c.index('def compute_invoice');j=c.index('PFX=')
new='''from decimal import ROUND_HALF_EVEN
def rb(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)
def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<0: raise ValueError('qty')
        if Decimal(str(l.get('unit_price')))<0: raise ValueError('price')
    sub=Decimal('0')
    for l in lines:
        if l['qty']==0: continue
        a=Decimal(l['qty'])*Decimal(str(l['unit_price']))
        if l['qty']>=200: a*=Decimal('0.88')
        elif l['qty']>=50: a*=Decimal('0.95')
        sub+=a
    disc=sub*TIER.get(customer.get('tier'),Decimal('0'))
    tax=(sub-disc)*Decimal('0.10')
    if customer.get('tax_exempt') is True: tax=Decimal('0')
    s,d,t=rb(sub),rb(disc),rb(tax)
    return {'subtotal':str(s),'discount':str(d),'tax':str(t),'total':str(s-d+t)}


'''
open(p,'w').write(c[:i]+new+c[j:])
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2000:])