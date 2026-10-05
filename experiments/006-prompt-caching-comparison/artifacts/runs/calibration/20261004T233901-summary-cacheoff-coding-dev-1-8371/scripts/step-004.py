p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("""def discount_rate(lines, customer, subtotal):
    return Decimal('0')""","""def discount_rate(lines, customer, subtotal):
    return {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}.get(customer.get('tier'), Decimal('0'))""")
s=s.replace("""def tax_rate(customer):
    return Decimal('0.10')""","""def tax_rate(customer):
    return {'NZ': Decimal('0.15'), 'AU': Decimal('0.10'), 'US': Decimal('0')}.get(customer.get('region'), Decimal('0.12'))""")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage2 done: tier discount gold5 silver2; tax by region NZ15 AU10 US0 else12\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])