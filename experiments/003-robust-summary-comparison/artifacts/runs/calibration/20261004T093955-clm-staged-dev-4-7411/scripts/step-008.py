L=open('/task/fixtures/stage-3/logs/profile-svc.log').read().splitlines()
x=[(i+1,l[:120]) for i,l in enumerate(L) if 'pool' in l and '/22' in l];print(len(x),x[:2])