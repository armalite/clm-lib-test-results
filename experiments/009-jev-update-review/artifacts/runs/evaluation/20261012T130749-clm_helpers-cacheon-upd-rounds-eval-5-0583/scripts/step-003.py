import glob,json
out=[]
for f in sorted(glob.glob('/task/fixtures/round-01/logs/*.log')):
    L=open(f).read().splitlines()
    e=[(i+1,l) for i,l in enumerate(L) if 'ERROR' in l or 'pool' in l.lower()]
    print(f.split('/')[-1],len(e))
    for i,l in e[:4]:print(' ',i,l[:150])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. changes.md: CHG-110 APPLIED TLS ticket rotation hourly; CHG-113 APPLIED build 7.35.8 checkout-api sets db.pool_max=-4 (round-01/changes.md:5?); CHG-114 auth-svc no config. Logs: slow query WARNs everywhere (noise); search-api disk usage high /var/data 92-95% (round-01/logs/search-api.log:4,12).'}]}
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-01/changes.md').read().splitlines())