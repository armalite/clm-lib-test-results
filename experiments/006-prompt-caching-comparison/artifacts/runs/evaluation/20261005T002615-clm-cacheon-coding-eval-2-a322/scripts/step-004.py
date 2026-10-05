p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("taxrate=Decimal(0)","taxrate=Decimal('0.10')")
s=s.replace("def format_money(amount, currency):\n    raise NotImplementedError\n",'''PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in PREFIX: raise ValueError('currency')
    a=r2(Decimal(str(amount)))
    sign='-' if a<0 else ''
    return sign+PREFIX[currency]+str(abs(a))
''')
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'invoice/core.py: compute_invoice(lines,customer) r2 half-up per line, TIER dict gold .05 silver .02 on subtotal, taxrate 0.10 on (sub-disc), validation qty int>0 not bool, price>=0, nonempty; returns str dict subtotal/discount/tax/total. format_money(amount,currency) PREFIX dict NZD NZ$ AUD A$ USD US$, 2dp, -prefix, else ValueError. Stages 1-2 done.'}]},open('/task/workspace/context.json','w'))