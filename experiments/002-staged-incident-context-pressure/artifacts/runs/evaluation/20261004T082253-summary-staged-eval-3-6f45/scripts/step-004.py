open('/task/workspace/notes.md','w').write('S1: release notes 6.33.4-cb27 line5 tax-engine timeout 2500->750; line19 pool 48->10. returns-svc.log:161 first timeout 750ms (95 timeouts). deploys.log:3 deploy 08:16.\n')
b='/task/fixtures/stage-1/logs/'
E=open(b+'edge-gw.log').readlines()
for i,l in enumerate(E[:400],1):
 if ' 50' in l:print(i,l.strip()[:160]);break
L=open(b+'returns-svc.log').readlines()
for i,l in enumerate(L,1):
 if 'tax-engine' in l and 'timed out' not in l:print(i,l.strip()[:160]);break
for i,l in enumerate(L,1):
 if 'pool' in l:print(i,l.strip()[:160]);break