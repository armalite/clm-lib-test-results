import glob,re
for f in ['board.md','changes.md']:
    print(f);print(open('/task/fixtures/round-02/'+f).read())
for p in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
    for i,l in enumerate(open(p),1):
        if re.search(r'ERROR|FATAL|CRIT|429|timeout|exhaust|expired|OOM|disk|lag|NXDOMAIN',l,re.I):
            print(p.split('/')[-1],i,l.strip()[:160])