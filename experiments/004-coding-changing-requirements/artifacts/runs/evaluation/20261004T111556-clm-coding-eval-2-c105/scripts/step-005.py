import re,subprocess,sys,json
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("def tax_rate(customer):\n    return Decimal('0')","def tax_rate(customer):\n    return Decimal('0.10')")
s=s.replace("def format_money(amount, currency):\n    raise NotImplementedError","""PREFIX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}\n\n\ndef format_money(amount, currency):\n    if currency not in PREFIX:\n        raise ValueError('bad currency')\n    a = r2(Decimal(str(amount)))\n    sign = '-' if a < 0 else ''\n    return sign + PREFIX[currency] + str(abs(a))""")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1+2 done in invoice/core.py: compute_invoice (half-up line rounding r2, tier discount gold5/silver2 via discount_rate(customer,subtotal), tax_rate(customer)=0.10 on subtotal-disc, validation qty int>0, price>=0, nonempty). format_money(amount,currency) PREFIX dict NZ$/A$/US$, sign before prefix, ValueError otherwise.'}]},open('/task/workspace/context.json','w'))