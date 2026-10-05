import subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("def tax_rate(customer):\n    return Decimal('0.10')","REG={'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}\n\ndef tax_rate(customer):\n    return REG.get((customer or {}).get('region'), Decimal('0.12'))")
s=s.replace("    if q>=100:\n        a=a*Decimal('0.90')","    if q>=200:\n        a=a*Decimal('0.88')\n    elif q>=50:\n        a=a*Decimal('0.95')")
s=s.replace("    customer=customer or {}\n","    customer=customer or {}\n    if not lines:\n        raise ValueError('empty')\n    for l in lines:\n        q=l.get('qty')\n        if isinstance(q,bool) or not isinstance(q,int) or q<=0:\n            raise ValueError('qty')\n        if Decimal(str(l.get('unit_price')))<0:\n            raise ValueError('price')\n",1)
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])