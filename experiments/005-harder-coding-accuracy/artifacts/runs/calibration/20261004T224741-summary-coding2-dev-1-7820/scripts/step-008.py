p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace('sub=Decimal(0)\n','sub=Decimal(0)\n    elig=Decimal(0)\n',1)
s=s.replace('        sub+=r(amt)','        sub+=r(amt)\n        if q<100: elig+=r(amt)')
s=s.replace('disc=r(sub*rate)','disc=r(elig*rate)')
s=s.replace('tax=r((sub-disc)*Decimal("0.10"))','trate={"NZ":Decimal("0.15"),"US":Decimal(0)}.get(customer.get("region"),Decimal("0.10"))\n    tax=r((sub-disc)*trate)')
open(p,'w').write(s)
import subprocess,sys
q=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(q.stderr[-1500:])
open('/task/workspace/NOTES.md','a').write('stage4 done: tier on non-bulk lines only; tax NZ15 US0 else10\n')