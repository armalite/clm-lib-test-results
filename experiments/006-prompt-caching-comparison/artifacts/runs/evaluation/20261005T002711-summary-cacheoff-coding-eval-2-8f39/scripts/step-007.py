s=open('/task/workspace/invoice/core.py').read()
for k in ['platinum','q < 0','_amt(l)','0.90']: print(k, k in s)