I=open('/task/fixtures/stage-1/logs/ingress-a.log').readlines()
b=[i for i,l in enumerate(I,1) if 'status=503' in l]
print(b[:5]);print(I[b[0]-1].strip()[:200])
open('/task/workspace/notes.md','a').write('ingress 503 first at ingress-a.log:%d; 60 503s total\n'%b[0])