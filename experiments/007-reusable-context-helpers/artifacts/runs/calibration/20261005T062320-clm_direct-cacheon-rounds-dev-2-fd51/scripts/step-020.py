import re,glob
print(open('/task/fixtures/round-07/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|error|FATAL|SERVFAIL|cert|429|invalid',l,re.I):
            print(f.split('/')[-1],i,l.strip()[:150])