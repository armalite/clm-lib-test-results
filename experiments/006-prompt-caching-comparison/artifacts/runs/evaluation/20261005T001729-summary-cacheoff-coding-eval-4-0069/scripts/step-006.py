p='/task/workspace/invoice/core.py';s=open(p).read()
s=s.replace('        if l["qty"] >= 100:\n            amt *= Decimal("0.90")\n','        if l["qty"] >= 200:\n            amt *= Decimal("0.88")\n        elif l["qty"] >= 50:\n            amt *= Decimal("0.95")\n')
s=s.replace('def format_money(amount, currency):\n    raise NotImplementedError\n','''PREF = {"NZD": "NZ$", "AUD": "A$", "USD": "US$"}\n\ndef format_money(amount, currency):\n    if currency not in PREF:\n        raise ValueError("bad currency")\n    a = _r(Decimal(str(amount)))\n    sign = "-" if a < 0 else ""\n    return sign + PREF[currency] + str(abs(a))\n''')
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage3 done: format_money, bulk 200->0.88, 50->0.95.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2000:])