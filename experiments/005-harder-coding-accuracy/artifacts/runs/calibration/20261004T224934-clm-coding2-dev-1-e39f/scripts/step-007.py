import subprocess,sys,json
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    ship=Decimal(0)","    ship=Decimal('7.50') if sub-disc<Decimal('100.00') else Decimal('0.00')")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1-3 done in core.py: r2 rounding, validation (qty int>0 non-bool, price>=0, nonempty), bulk qty>=100 line*0.9 before r2, tier disc gold5%/silver2% of subtotal (r2), tax 10% on (sub-disc), ship 7.50 if sub-disc<100 else 0 (untaxed). tot=sub-disc+ship+tax. Output dict of str.'}]}
json.dump(c,open('/task/workspace/context.json','w'))