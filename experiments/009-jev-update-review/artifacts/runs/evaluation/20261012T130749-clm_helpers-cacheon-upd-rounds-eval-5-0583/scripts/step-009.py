import json
c=json.load(open('/task/workspace/context.json'))
keep=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
keep.append({'id':'n4','role':'note','body':'R3 logs: auth-svc tls handshake failed peer=bank-api certificate_expired (round-03/logs/auth-svc.log:1,16,21,25,35,62) -> board says MEMORY_LEAK but evidence suggests CERT_EXPIRED; watch for board correction. Next: advance to R4.'})
c['entries']=keep
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')