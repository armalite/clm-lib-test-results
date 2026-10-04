Q=open('/task/fixtures/stage-3/logs/quotes-api.log').read().splitlines()
h=[i+1 for i,l in enumerate(Q) if '22/22' in l];print(len(h),h[:3])
if h:print(Q[h[0]-1][:160])