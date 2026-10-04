import re
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("        sub+=r2(q*p)","        a=q*p\n        if q>=100: a=a*Decimal('0.90')\n        sub+=r2(a)")
s=s.replace("    disc=Decimal(0)\n","    rate={'gold':Decimal('0.05'),'silver':Decimal('0.02')}.get((customer or {}).get('tier'),Decimal(0))\n    disc=r2(sub*rate)\n")
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1+2 done in core.py: r2 rounding, validation (qty int>0 non-bool, price>=0, nonempty), bulk qty>=100 line*0.9 before r2, tier disc gold5%/silver2% of subtotal (r2), tax 10% on (sub-disc), ship 0 placeholder. Output dict of str.'}]}
json.dump(c,open('/task/workspace/context.json','w'))