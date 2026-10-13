import os,re
b='/task/fixtures/round-02/'
print(open(b+'changes.md').read())
print(open(b+'board.md').read())
for f in sorted(os.listdir(b+'logs')):
    for i,l in enumerate(open(b+'logs/'+f),1):
        if 'slow query' in l: continue
        if re.search(r'ERROR|WARN|FATAL|429|fail|expired|OOM|lag|disk|pool',l,re.I): print(f,i,l.strip()[:160])