import collections,re
b='/task/fixtures/stage-1/logs/'
L=open(b+'quotes-api.log').readlines()
c=collections.Counter(re.sub(r'[0-9a-f]{6,}|\d+','N',' '.join(l.split()[1:])[:90]) for l in L if 'ERROR' in l or 'WARN' in l)
for k,v in c.most_common(8):print(v,k)
L=open(b+'ingress-a.log').readlines();print(L[0][:200]);print(collections.Counter(l.split()[3] if len(l.split())>3 else '' for l in L).most_common(6))