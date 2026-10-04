import subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    tax=r2((sub-disc)*rate)","    tax=r2((sub-disc)*rate)\n    if customer.get('tax_exempt') is True: tax=Decimal('0.00')")
s=s.replace("str(abs(a))","'{:,.2f}'.format(r2(abs(a)))")
open(p,'w').write(s)
print(s[s.find('def format_money'):])
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])