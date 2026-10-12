import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']=n['body'].replace(' (but checkout logs showed pool exhausted; verify R8 logs)','')+' R8 logs: no checkout errors (Thread D false alarm OK); auth-svc tls handshake failed bank-api round-08/logs/auth-svc.log:6,9,29,58,85. Next: advance R9.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')