import subprocess,sys,json
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    sub=Decimal(0)\n","    sub=Decimal(0); elig=Decimal(0)\n")
s=s.replace("        sub+=r2(a)\n","        sub+=r2(a)\n        if q<100: elig+=r2(a)\n")
s=s.replace("disc=r2(sub*rate)","disc=r2(elig*rate)")
s=s.replace("tax=r2((sub-disc)*Decimal('0.10'))","trate={'NZ':Decimal('0.15'),'US':Decimal(0)}.get((customer or {}).get('region'),Decimal('0.10'))\n    tax=r2((sub-disc)*trate)")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1-4 done in invoice/core.py compute_invoice(lines,customer): r2 HALF_UP, validation (qty int>0 non-bool, price>=0, nonempty), bulk qty>=100 line*0.9 before r2, tier disc gold5%/silver2% of non-bulk lines sum (elig, r2), tax rate NZ15%/US0%/else10% on (sub-disc), ship 7.50 if sub-disc<100 else 0 (untaxed). tot=sub-disc+ship+tax. Output dict of str keys subtotal,discount,shipping,tax,total.'}]}
json.dump(c,open('/task/workspace/context.json','w'))