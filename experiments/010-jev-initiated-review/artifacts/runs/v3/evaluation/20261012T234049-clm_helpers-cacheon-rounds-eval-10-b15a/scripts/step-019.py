import re,glob
print(open('/task/fixtures/round-07/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
    ls=[i for i,l in enumerate(open(f),1) if re.search(r'ERROR|WARN|FATAL|fail|429',l) and 'slow' not in l]
    print(f.split('/')[-1],len(ls),ls[:3],ls[-1:] if ls else '')
    if ls: print(open(f).readlines()[ls[0]-1][:200])