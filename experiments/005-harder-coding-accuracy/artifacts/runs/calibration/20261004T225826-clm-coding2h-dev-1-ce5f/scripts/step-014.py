import subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("{'gold':Decimal('0.05'),'silver':Decimal('0.02')}","{'gold':Decimal('0.08'),'silver':Decimal('0.02'),'platinum':Decimal('0.10')}")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])