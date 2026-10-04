p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace('sub+=r(q*p)','amt=q*p\n        if q>=100: amt=amt*Decimal("0.90")\n        sub+=r(amt)')
s=s.replace('disc=Decimal(0)\n','rate={"gold":Decimal("0.05"),"silver":Decimal("0.02")}.get(customer.get("tier"),Decimal(0))\n    disc=r(sub*rate)\n')
open(p,'w').write(s)
import subprocess,sys
q=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(q.stderr[-1500:])
open('/task/workspace/NOTES.md','a').write('stage2 done: tier disc gold5 silver2 on subtotal; bulk qty>=100 x0.9\n')