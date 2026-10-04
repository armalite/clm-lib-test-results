p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    t=r((sub-d)*tax_rate(customer))","    t=r((sub-d)*tax_rate(customer))\n    if customer.get('tax_exempt') is True: t=Decimal('0.00')")
s=s.replace("PREFIX[currency]+str(abs(a))","PREFIX[currency]+'{:,.2f}'.format(abs(a))")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('Stage4 done: tax_exempt, comma format.\n')
import subprocess,sys
q=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(q.stderr[-1500:])
import sys;sys.path.insert(0,'/task/workspace')
from invoice import format_money as f
print(f('1234.5','NZD'),f('-1234567.555','USD'),f('5','AUD'))