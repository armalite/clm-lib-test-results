import re,glob
for f in sorted(glob.glob('/task/fixtures/round-10/logs/*.log')):
    n=0
    for i,l in enumerate(open(f),1):
        if re.search(r'batch_size|disk|429|heap',l,re.I) and n<4:
            print(f.split('/')[-1],i,l.strip()[:120]);n+=1
print(open('/task/fixtures/round-10/board.md').read())