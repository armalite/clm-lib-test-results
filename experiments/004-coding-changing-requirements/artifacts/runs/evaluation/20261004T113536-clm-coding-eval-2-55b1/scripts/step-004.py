p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("def tax_rate(customer, lines):\n    return Decimal('0')","def tax_rate(customer, lines):\n    return Decimal('0.10')")
s=s.replace("def format_money(amount, currency):\n    raise NotImplementedError","PREFIX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}\n\n\ndef format_money(amount, currency):\n    if currency not in PREFIX:\n        raise ValueError('bad currency')\n    a = r2(Decimal(str(amount)))\n    sign = '-' if a < 0 else ''\n    return f'{sign}{PREFIX[currency]}{abs(a):.2f}'")
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
print(open('/task/workspace/invoice/__init__.py').read())
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1+2 done: invoice/core.py has r2(), discount_rate(customer,sub,lines) tier gold5%/silver2%, tax_rate()=0.10, validation (empty, qty pos int, price>=0), format_money with PREFIX dict (NZD/AUD/USD), neg sign before prefix.'}]}
json.dump(c,open('/task/workspace/context.json','w'))