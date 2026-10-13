import sys,subprocess,re;sys.path.insert(0,'/task/workspace')
p='/task/workspace/exporter/core.py';s=open(p).read()
print([l for l in s.split('\n') if 'archived' in l or 'strip' in l])
import importlib,reghelper as H
reg={'S2.1':'only active unless include_archived','S2.3':'strip title','S1.2':'scope','S1.3':'confidential'}
new={'S4.1':'include_archived honoured only for admin','S4.2':'collapse internal whitespace runs in titles'}
print(H.decide(H.affected(reg,new),0.5))