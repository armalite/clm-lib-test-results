p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("""def discount_rate(lines, customer, subtotal):
    return Decimal('0')""","""def discount_rate(lines, customer, subtotal):
    return {'gold':Decimal('0.05'),'silver':Decimal('0.02')}.get(customer.get('tier'),Decimal('0'))""")
s=s.replace("""def tax_rate(customer):
    return Decimal('0.10')""","""def tax_rate(customer):
    return {'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(customer.get('region'),Decimal('0.12'))""")
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'summary','body':'invoice/core.py: _r (2dp half up), _validate, discount_rate(lines,customer,subtotal), tax_rate(customer), compute_invoice, format_money (NotImplemented). Stage1: per-line rounding, validation (empty, qty pos int, price>=0). Stage2 done: tier gold5%/silver2%; tax region NZ15 AU10 US0 else12. Next: advance to stage 3.'}]}
json.dump(c,open('/task/workspace/context.json','w'))