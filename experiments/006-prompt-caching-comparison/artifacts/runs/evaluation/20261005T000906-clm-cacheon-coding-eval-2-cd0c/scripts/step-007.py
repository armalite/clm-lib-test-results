import subprocess,sys,json
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}","TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}")
s=s.replace("q<=0:\n            raise ValueError('qty')","q<0:\n            raise ValueError('qty')\n        if q==0:\n            continue")
s=s.replace("sub+=_r(q*p)","amt=q*p\n        if q>=100:\n            amt=amt*Decimal('0.90')\n        sub+=_r(amt)")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2500:])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stages1-3 in invoice/core.py: compute_invoice (half-up line rounding _r, bulk qty>=100 x0.90 before rounding, TIER platinum10/gold7/silver3%, qty0 skipped (price check before skip), qty<0/empty/neg price ValueError, tax 10% on sub-disc, str fields); format_money PFX NZ$/A$/US$, - before prefix, ValueError unknown. Next: if tests OK, advance to stage 4.'}]}
json.dump(c,open('/task/workspace/context.json','w'))