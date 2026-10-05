p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("disc=_r(sub*Decimal(0))","disc=_r(sub*{'gold':Decimal('0.05'),'silver':Decimal('0.02')}.get(customer.get('tier'),Decimal(0)))")
s=s.replace("tax=_r((sub-disc)*Decimal('0.10'))","tax=_r((sub-disc)*{'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal(0)}.get(customer.get('region'),Decimal('0.12')))")
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
c={'format':'clm-context/v1','entries':[{'id':'sum1','role':'summary','body':'Stage1+2 done in invoice/core.py: compute_invoice w/ _r half-up rounding per line, validation (empty, qty pos int non-bool, price>=0), tier discount dict gold .05 silver .02, region tax dict NZ .15 AU .10 US 0 else .12. format_money still NotImplemented. Next: advance to stage 3.'}]}
json.dump(c,open('/task/workspace/context.json','w'))