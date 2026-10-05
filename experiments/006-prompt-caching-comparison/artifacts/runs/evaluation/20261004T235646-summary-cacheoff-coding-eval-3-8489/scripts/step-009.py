p='/task/workspace/invoice/core.py'
c=open(p).read()
c=c.replace("    return Decimal('0.10')","    return {'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(customer.get('region'),Decimal('0.12'))")
c=c.replace("    if q>=100: a=a*Decimal('0.90')","    if q>=200: a=a*Decimal('0.88')\n    elif q>=50: a=a*Decimal('0.95')")
c=c.replace("def compute_invoice(lines, customer):\n","def compute_invoice(lines, customer):\n    if not lines: raise ValueError('empty')\n    for l in lines:\n        q=l.get('qty')\n        if isinstance(q,bool) or not isinstance(q,int) or q<=0: raise ValueError('qty')\n        if Decimal(str(l['unit_price']))<0: raise ValueError('price')\n")
open(p,'w').write(c)
open('/task/workspace/NOTES.md','a').write('Stage4 done.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2000:])