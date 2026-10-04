p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("l['qty']>=100","l['qty']>=50").replace("l['qty']<100","l['qty']<50")
open(p,'w').write(s)
print(s[s.find('def validate'):s.find('def compute')])
print(s[s.find('def compute'):s.find('amounts=')])