import subprocess,sys,json
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace('RATES={"gold":Decimal("0.05"),"silver":Decimal("0.02")}','RATES={"platinum":Decimal("0.10"),"gold":Decimal("0.07"),"silver":Decimal("0.03")}')
s=s.replace('q<=0: raise ValueError("qty")','q<0: raise ValueError("qty")')
s=s.replace('        sub+=r(q*p)','        if q==0: continue\n        a=q*p\n        if q>=100: a=a*Decimal("0.90")\n        sub+=r(a)')
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2000:])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'core.py: r()=quantize half-up; RATES tier dict (stage3: platinum10 gold7 silver3); compute_invoice: validation (neg qty/empty/neg price ValueError, qty0 skipped, qty must be int), bulk qty>=100 line*0.90 before rounding, tier discount, tax 10% on sub-d; format_money PFX NZ$/A$/US$, - prefix, else ValueError. Stage 3 implemented; if tests pass next: advance to stage 4.'}]}
json.dump(c,open('/task/workspace/context.json','w'))