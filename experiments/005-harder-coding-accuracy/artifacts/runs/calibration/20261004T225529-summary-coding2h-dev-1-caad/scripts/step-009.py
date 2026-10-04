p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    sub=Decimal(0)\n","    sub=Decimal(0); tier_elig=Decimal(0)\n")
s=s.replace("        sub+=r(a)\n","        sub+=r(a)\n        if q<100: tier_elig+=r(a)\n")
s=s.replace("    tier_elig=sub\n","")
s=s.replace("tax=r((sub-disc)*Decimal('0.10'))","rate={'NZ':Decimal('0.15'),'US':Decimal(0)}.get(customer.get('region'),Decimal('0.10'))\n    tax=r((sub-disc)*rate)")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage4: bulk lines not tier-eligible; tax NZ15 US0 else10\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])