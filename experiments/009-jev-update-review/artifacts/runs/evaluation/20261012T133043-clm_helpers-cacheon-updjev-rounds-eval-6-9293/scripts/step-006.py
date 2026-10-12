import os
d='/task/fixtures/round-02/logs'
print(os.listdir(d))
p=d+'/pricing-svc.log'
if os.path.exists(p):
  for i,l in enumerate(open(p),1):
    if any(k in l for k in ('ERROR','batch','WARN')): print(i,l.strip()[:160])