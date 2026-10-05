import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1']
n.append({'id':'n2','role':'note','body':'R2: board.md:3 Thread A DNS_RESOLUTION inventory-svc + checkout-api (status line truncated, check). changes.md:3 CHG-120 APPLIED search-api http.max_inflight=-1 (watch BAD_CONFIG). changes.md:4 CHG-121 auth-svc no config. checkout-api DNS SERVFAIL rates.internal lines 8,24,29,38,46,59; inventory lines 8-74.'})
c['entries']=n
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-02/board.md').read()[:1500])