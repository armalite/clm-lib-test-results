import json
p='/task/workspace/context.json'
d=json.load(open(p))
n=[e for e in d['entries'] if e['id']=='notes'][0]['body']
n=n.replace(' Next: advance to R6.','')
n+='\nR6: board.md:3 Thread B now also search-api (cause DB_POOL per board, status ongoing). Logs: CERT_EXPIRED sso.example.net search-api.log:11,14,25,26,35,51,54,63; shipping-svc.log:4,35,40,45,51,57,62,78. No lag/other errors. Next: advance to R7.'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open(p,'w'))
print('ok')