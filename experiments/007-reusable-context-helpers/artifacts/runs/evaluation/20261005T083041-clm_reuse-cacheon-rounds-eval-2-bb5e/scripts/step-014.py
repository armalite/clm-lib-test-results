import ctx,re
L=open('/task/fixtures/round-05/logs/ledger-svc.log').read().splitlines()
x=[i for i,l in enumerate(L,1) if 'SERVFAIL' in l]
print(len(x),x[:3],x[-3:])
d=ctx.load();d['entries']=[e for e in d['entries'] if e['id'] in('n1','n2','n3','n4')]+[{'id':'n5','role':'note','body':'R5: board empty (no changes). ledger DNS SERVFAIL rates.internal continues ledger-svc.log lines %s (count %d). auth/payments no heap warns now (mitigated holds). Others only slow-query noise.'%(x[:1]+x[-1:],len(x))}];ctx.save(d);print('ok')