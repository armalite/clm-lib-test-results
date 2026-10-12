import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
    L=open(f).read().splitlines()
    errs=[(i+1,l[:120]) for i,l in enumerate(L) if re.search('ERROR|disk|pool|certificate|mem',l)]
    print(f.split('/')[-1],len(errs))
    for e in errs[:2]+errs[-1:]: print(' ',e)
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR4 logs: auth-svc cert_expired bank-api continues (round-04/logs/auth-svc.log:3,55); others clean.\nR5: board.md:3 OPEN CAPACITY_REVIEW.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))