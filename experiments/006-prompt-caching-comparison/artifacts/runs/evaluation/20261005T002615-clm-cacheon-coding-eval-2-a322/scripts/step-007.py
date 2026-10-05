p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}","TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}")
s=s.replace("q<=0: raise ValueError('qty')","q<0: raise ValueError('qty')")
s=s.replace("        sub+=r2(q*p)","        if q==0: continue\n        amt=q*p\n        if q>=100: amt=amt*Decimal('0.90')\n        sub+=r2(amt)")
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'invoice/core.py: compute_invoice(lines,customer) per line: qty int not bool, <0 ValueError, 0 skipped (price still validated first), price>=0, nonempty lines; amt=q*p, *0.90 if q>=100, r2 half-up, summed. TIER platinum .10 gold .07 silver .03 on subtotal; tax 0.10 on (sub-disc); returns str dict subtotal/discount/tax/total. format_money(amount,currency) PREFIX NZD NZ$ AUD A$ USD US$, 2dp, -prefix, else ValueError. Stages 1-3 done (step 7). Next: advance to stage 4.'}]},open('/task/workspace/context.json','w'))