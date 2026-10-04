p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}","TIER={'gold':Decimal('0.08'),'silver':Decimal('0.02'),'platinum':Decimal('0.10')}\nTAX={'NZ':Decimal('0.15'),'US':Decimal('0')}")
s=s.replace("tax=r((subtotal-discount)*Decimal('0.10'))","tax=r((subtotal-discount)*TAX.get(customer.get('region'),Decimal('0.10')))")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
open('/task/workspace/NOTES.md','a').write('\nstage5: bulk>=50, qty0 ignored. stage6: gold 8% platinum 10%, tax NZ15 US0 else 10. done.\n')