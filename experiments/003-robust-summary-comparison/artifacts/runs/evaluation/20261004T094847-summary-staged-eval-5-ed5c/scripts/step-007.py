import os,glob
for f in glob.glob('/task/fixtures/stage-2/**/*',recursive=True):
  if os.path.isfile(f): print(f)
for f in glob.glob('/task/fixtures/stage-2/logs/*.log'):
  n=0
  for i,l in enumerate(open(f),1):
    if 'pool exhausted' in l or 'status=503' in l:
      print(f.split('stage-2/')[1],i,l[:140].rstrip());n+=1
      if n>2:break
