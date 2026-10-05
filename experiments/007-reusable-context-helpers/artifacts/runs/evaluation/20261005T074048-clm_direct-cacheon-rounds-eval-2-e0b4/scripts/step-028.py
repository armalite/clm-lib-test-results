import re,glob
print(open('/task/fixtures/round-09/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|error|SERVFAIL|expired|429|FATAL',l): print(f.split('/')[-1],i,l.strip()[:150])