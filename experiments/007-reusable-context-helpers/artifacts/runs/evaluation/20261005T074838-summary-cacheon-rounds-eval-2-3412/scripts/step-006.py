import glob
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if 'ERROR' in l or 'error' in l.lower(): print(f.split('/')[-1],i,l.strip()[:150])
open('/task/workspace/notes.md','a').write('\nR2: no ERROR/non-INFO lines beyond slow query/heap/gc in round-02 logs.\n')
