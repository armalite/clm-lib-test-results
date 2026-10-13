import re,glob
print(open('/task/fixtures/round-09/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
    L=[(i,l) for i,l in enumerate(open(f),1) if re.search(r'ERROR|WARN|FATAL|fail|429',l) and 'slow' not in l]
    print(f.split('/')[-1],len(L),[i for i,_ in L][:3],[i for i,_ in L][-1:] if L else '')
    for i,l in L[:2]: print(' ',i,l.strip()[:160])