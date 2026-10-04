L=open('/task/fixtures/stage-3/logs/quotes-api.log').read().splitlines()
r=[i for i,l in enumerate(L,1) if '22/22' in l]
print(len(r),r[:3])