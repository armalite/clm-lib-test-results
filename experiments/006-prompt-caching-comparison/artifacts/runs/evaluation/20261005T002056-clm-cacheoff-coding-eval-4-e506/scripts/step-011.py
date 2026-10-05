import json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
a=s.index('def compute_invoice');b=s.index('PFX=')
new='''def compute_invoice(lines, customer):
    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<0: raise ValueError('qty')
        if Decimal(str(l.get('unit_price')))<0: raise ValueError('price')
    sub=Decimal(0)
    for l in lines:
        if l['qty']==0: continue
        a=Decimal(l['qty'])*Decimal(str(l['unit_price']))
        if l['qty']>=200: a*=Decimal('0.88')
        elif l['qty']>=50: a*=Decimal('0.95')
        sub+=a
    disc=sub*TIER.get(customer.get('tier'),Decimal(0))
    rate=Decimal('0.10')
    tax=(sub-disc)*rate
    if customer.get('tax_exempt') is True: tax=Decimal(0)
    rs,rd,rt=(x.quantize(Q,rounding=ROUND_HALF_EVEN) for x in (sub,disc,tax))
    tot=rs-rd+rt
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(tot.quantize(Q))}


'''
s=s[:a]+new+s[b:]
s=s.replace('ROUND_HALF_UP\n','ROUND_HALF_UP, ROUND_HALF_EVEN\n',1)
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','s9.obs')]
c['entries'][0]['body']+=' Stage4 applied (half-even exact rounding, tax_exempt, qty0 skip).'
json.dump(c,open('/task/workspace/context.json','w'))