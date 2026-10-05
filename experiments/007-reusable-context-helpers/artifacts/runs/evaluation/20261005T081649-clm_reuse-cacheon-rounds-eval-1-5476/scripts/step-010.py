import glob,re
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|FATAL|429|OOM|disk|cert|dns|pool',l,re.I) and 'slow' not in l.lower():
            print(f.split('/')[-1],i,l.strip()[:150])