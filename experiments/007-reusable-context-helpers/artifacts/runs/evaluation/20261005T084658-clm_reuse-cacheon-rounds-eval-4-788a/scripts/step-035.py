import os
b='/task/fixtures/round-11/logs/'
for f in sorted(os.listdir(b)):
  for i,l in enumerate(open(b+f),1):
    if any(k in l for k in ('config','429','pool','ERROR')):print(f,i,l[:90].strip())