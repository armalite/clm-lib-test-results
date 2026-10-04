import json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}","TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}")
s=s.replace("q<=0: raise ValueError('qty')","q<0: raise ValueError('qty')")
s=s.replace("        sub+=r2(q*p)","        if q==0: continue\n        a=q*p\n        if q>=100: a=a*Decimal('0.90')\n        sub+=r2(a)")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'invoice/core.py: compute_invoice(lines,customer)->dict str 2dp subtotal/discount/tax/total; line r2 half-up; qty>=100 line*0.90 before round; qty0 skipped, neg qty/neg price/empty ValueError; tier platinum10/gold7/silver3%; tax 10% on sub-disc; format_money(amount,cur) NZ$/A$/US$, - prefix neg, else ValueError. Stages 1-3 done (check tests result below).'}]}
json.dump(c,open('/task/workspace/context.json','w'))