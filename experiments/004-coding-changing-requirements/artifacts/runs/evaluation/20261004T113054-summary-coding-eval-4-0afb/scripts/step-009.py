import subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
a=s.index('def compute_invoice');b=s.index('CUR=')
new='''def compute_invoice(lines, customer):
    from decimal import ROUND_HALF_EVEN
    def be(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)
    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<0: raise ValueError('qty')
        try: up=Decimal(str(l['unit_price']))
        except Exception: raise ValueError('price')
        if not up.is_finite() or up<0: raise ValueError('price')
    sub=Decimal(0)
    for l in lines:
        if l['qty']==0: continue
        a=Decimal(l['qty'])*Decimal(str(l['unit_price']))
        if l['qty']>=200: a*=Decimal('0.88')
        elif l['qty']>=50: a*=Decimal('0.95')
        sub+=a
    disc=sub*TIER.get(customer.get('tier'),Decimal(0))
    tax=(sub-disc)*tax_rate(customer, sub)
    if customer.get('tax_exempt') is True: tax=Decimal(0)
    rs,rd,rt=be(sub),be(disc),be(tax)
    tot=rs-rd+rt
    return {k:str(be(v)) for k,v in dict(subtotal=rs,discount=rd,tax=rt,total=tot).items()}

'''
open(p,'w').write(s[:a]+new+s[b:])
open('/task/workspace/NOTES.md','a').write('stage4 done\n')
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2000:])