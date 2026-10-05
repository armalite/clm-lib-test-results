p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("{'gold':Decimal('0.05'),'silver':Decimal('0.02')}","{'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage4 done: format_money, tiers plat10 gold7 silver3.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])
print(open('/task/workspace/invoice/__init__.py').read())