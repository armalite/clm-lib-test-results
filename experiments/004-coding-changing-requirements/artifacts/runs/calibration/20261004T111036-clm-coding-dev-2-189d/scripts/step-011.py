p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    return Decimal('0.10')\n","    return REG.get(customer.get('region'),Decimal('0.12'))\n\nREG={'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}\n",1)
s=s.replace("r2(int(l['qty'])*Decimal(str(l['unit_price'])))","r2(int(l['qty'])*Decimal(str(l['unit_price']))*(Decimal('0.90') if int(l['qty'])>=100 else 1))")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2500:])