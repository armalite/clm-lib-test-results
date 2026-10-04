b='/task/fixtures/stage-2/'
L=open(b+'logs/shipping-api.log').readlines()
for i in [254,257,268]:print(i,L[i-1].rstrip()[:160])
I=open(b+'logs/ingress-a.log').readlines()
n=[i for i,l in enumerate(I,1) if ' 503' in l or 'status=503' in l]
print(len(n),n[:3]);print(I[n[0]-1][:200] if n else '')
open('/task/workspace/notes.txt','a').write('\nstage2: changes.log:2 CHG-5161 APPLIED timeout 4000; db pool exhausted errors shipping-api.log:254; pool 12 from release-notes:13; candidate DB_POOL_EXHAUSTED value 12\n')