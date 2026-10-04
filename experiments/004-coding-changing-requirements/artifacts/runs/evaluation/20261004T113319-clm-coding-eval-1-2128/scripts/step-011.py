import subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("def _tax_rate(customer):\n    return Decimal('0.10')","def _tax_rate(customer):\n    c = customer or {}\n    if c.get('tax_exempt') is True:\n        return Decimal('0')\n    return {'NZ': Decimal('0.15'), 'AU': Decimal('0.10'), 'US': Decimal('0')}.get(c.get('region'), Decimal('0.12'))")
s=s.replace("def format_money(amount, currency):\n    raise NotImplementedError","def format_money(amount, currency):\n    pre = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}.get(currency)\n    if pre is None:\n        raise ValueError('bad currency')\n    a = Decimal(str(amount)).quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)\n    sign = '-' if a < 0 else ''\n    return sign + pre + str(abs(a))")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])