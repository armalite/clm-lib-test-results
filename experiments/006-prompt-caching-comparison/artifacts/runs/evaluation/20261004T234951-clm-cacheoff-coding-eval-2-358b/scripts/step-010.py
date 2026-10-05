import subprocess,sys,json
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("def tax_rate(customer):\n    return Decimal('0.10')","def tax_rate(customer):\n    if customer.get('tax_exempt') is True:\n        return Decimal('0')\n    return Decimal('0.10')")
s=s.replace("return sign+PREFIX[currency]+str(abs(a))","return sign+PREFIX[currency]+'{:,.2f}'.format(abs(a))")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'All 4 stages implemented in invoice/core.py (stage4: tax_exempt True -> tax 0; format_money comma thousands). Next: final if tests ok.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))