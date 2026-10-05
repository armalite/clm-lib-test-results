import re,glob
print(open('/task/fixtures/round-07/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
    ls=[(i+1,l) for i,l in enumerate(open(f)) if re.search(r'ERROR|error|FATAL',l)]
    print(f.split('/')[-1],len(ls),ls[0][0] if ls else '',ls[-1][0] if ls else '')
    if ls: print(' ',ls[0][1][:200].strip())