p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}","TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}")
s=s.replace("or q<=0: raise ValueError('qty')","or q<0: raise ValueError('qty')")
s=s.replace("        sub+=r(q*p)","        if q==0: continue\n        amt=q*p\n        if q>=100: amt=amt*Decimal('0.90')\n        sub+=r(amt)")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('Stage3 done: bulk 0.90 qty>=100, tiers plat10/gold7/silver3, qty0 skipped (price still validated before skip).\n')
import subprocess,sys
q=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(q.stderr[-1500:])
print(s[:1200])