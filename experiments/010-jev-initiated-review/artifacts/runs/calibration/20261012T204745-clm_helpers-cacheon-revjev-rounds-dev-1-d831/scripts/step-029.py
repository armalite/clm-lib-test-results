import re,glob
for f in ['board.md','changes.md']:
    for i,l in enumerate(open('/task/fixtures/round-10/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-10/logs/*')):
    hits=[i for i,l in enumerate(open(f),1) if re.search(r'ERROR|429|exhaust|max_inflight',l)]
    print(f.split('/')[-1],hits[:15])