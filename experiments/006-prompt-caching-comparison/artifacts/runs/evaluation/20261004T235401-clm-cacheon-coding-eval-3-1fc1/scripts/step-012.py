import glob
for f in sorted(glob.glob('/task/fixtures/stage-*/REQUIREMENTS.md')):
  for n,l in enumerate(open(f),1):
    if any(k in l.lower() for k in ['round','format','half','comma']): print(f[15:23],n,l.strip()[:300])
import subprocess
for n,l in enumerate(open('/task/workspace/invoice/core.py'),1):
  if any(k in l for k in ['ROUND','quantize','def format','NZ$','-']): print(n,l.rstrip()[:150])