p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}","TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}")
s=s.replace("q<=0:","q<0:")
s=s.replace("sub=sum((_r(l['qty']*Decimal(str(l['unit_price']))) for l in lines),Decimal('0'))","sub=sum((_r(l['qty']*Decimal(str(l['unit_price']))*(Decimal('0.90') if l['qty']>=100 else 1)) for l in lines if l['qty']!=0),Decimal('0'))")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])
open('/task/workspace/NOTES.md','w').write('stage1-3 done in core.py: rounding half up, tiers plat10/gold7/silver3, tax10%, format_money, bulk qty>=100 x0.9, qty0 skipped\n')