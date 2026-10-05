p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    tax=_r((sub-disc)*taxrate)","    tax=_r((sub-disc)*taxrate)\n    if customer.get('tax_exempt') is True:\n        tax=Decimal('0.00')")
s=s.replace("str(abs(a))","'{:,.2f}'.format(abs(a))")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage4 done: tax_exempt, comma sep.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
import sys;sys.path.insert(0,'/task/workspace')
from invoice import format_money as f;print(f('1234.5','NZD'),f('-1234567.005','USD'))