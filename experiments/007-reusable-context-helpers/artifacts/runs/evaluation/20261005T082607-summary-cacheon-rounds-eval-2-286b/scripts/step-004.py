import glob,re
b='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
    print('==',f);print(open(b+f).read())
for f in sorted(glob.glob(b+'logs/*.log')):
    print('==',f.split('/')[-1])
    for i,l in enumerate(open(f),1):
        if 'slow query' in l: continue
        if re.search(r'ERROR|WARN|FATAL|429|cert|dns|pool|lag|disk|OOM|restart|config',l,re.I):
            print(i,l.rstrip()[:150])
