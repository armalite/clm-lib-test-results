import subprocess,sys
p='/task/workspace/invoice/core.py'
c=open(p).read()
c=c.replace("    return Decimal('0.10')\n","    return {'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(customer.get('region'),Decimal('0.12'))\n")
c=c.replace("    sub=sum((Decimal(str(l['qty']))*Decimal(str(l['unit_price']))*(Decimal('0.90') if Decimal(str(l['qty']))>=100 else 1) for l in lines), Decimal('0'))","""    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')
        if Decimal(str(l.get('unit_price')))<0: raise ValueError('price')
    def _f(q): return Decimal('0.88') if q>=200 else (Decimal('0.95') if q>=50 else Decimal(1))
    sub=sum((Decimal(l['qty'])*Decimal(str(l['unit_price']))*_f(l['qty']) for l in lines), Decimal('0'))""")
open(p,'w').write(c)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])