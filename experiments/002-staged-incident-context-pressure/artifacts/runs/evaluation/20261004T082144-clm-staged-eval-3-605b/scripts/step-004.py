import json
b='/task/fixtures/stage-1/'
L=open(b+'logs/returns-svc.log').read().splitlines()
t=[i for i,l in enumerate(L,1) if 'timed out' in l]
p=[i for i,l in enumerate(L,1) if 'pool' in l.lower()]
print(len(t),t[:3],t[-3:]);print(p)
print(open(b+'UPDATE.md').read());print(open(b+'ops/oncall-notes.md').read())
n='Stage1: deploys.log:3 returns-svc 6.33.4-cb27 at 08:16:14. release-notes-6.33.4-cb27.md:5 tax-engine timeout_ms 2500->750; :19 db.pool.max_size 48->10. config yaml:7 timeout 2500, :11 pool 48. Symptom returns-svc.log:161-179 tax-engine timed out after 750ms (many). pool waits only 7 lines (e.g. :193 in_use 10/10). Noise: gc, disk, dns, tls.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))