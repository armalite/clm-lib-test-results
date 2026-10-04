p='/task/workspace/invoice/core.py'
c=open(p).read()
c=c.replace("def tax_rate(customer):\n    return Decimal('0.10')","def tax_rate(customer):\n    return {'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(customer.get('region'),Decimal('0.12'))\n\ndef bulk(q):\n    return Decimal('0.88') if q>=200 else (Decimal('0.95') if q>=50 else Decimal('1'))\n\ndef validate(lines):\n    if not lines: raise ValueError('empty')\n    for l in lines:\n        q=l.get('qty')\n        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')\n        if Decimal(str(l.get('unit_price')))<0: raise ValueError('price')")
c=c.replace("    sub=sum((Decimal(str(l['qty']))*Decimal(str(l['unit_price']))*(Decimal('0.90') if Decimal(str(l['qty']))>=100 else 1) for l in lines), Decimal('0'))","    validate(lines)\n    sub=sum((Decimal(str(l['qty']))*Decimal(str(l['unit_price']))*bulk(l['qty']) for l in lines), Decimal('0'))")
open(p,'w').write(c)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])