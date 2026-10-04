p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("def tax_rate(customer): return Decimal('0.10')","def tax_rate(customer): return {'NZ':Decimal('0.15'),'US':Decimal('0')}.get((customer or {}).get('region'),Decimal('0.10'))")
s=s.replace("discounts=[tier_rate(customer)*subtotal]","elig=sum((a for a,l in zip(amounts,lines) if l['qty']<100),Decimal(0))\n    discounts=[tier_rate(customer)*elig]")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])