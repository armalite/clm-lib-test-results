import re
b='/task/fixtures/stage-1/logs/'
L=open(b+'quotes-api.log').readlines()
n=[i for i,l in enumerate(L,1) if 'rates-svc timed out' in l]
print(n[:3],n[-1]);print(L[n[0]-1].strip()[:200])
I=open(b+'ingress-a.log').readlines()
m=[i for i,l in enumerate(I,1) if re.search(r'status=5|\s50[0-9]\s',l)]
print(len(m),m[:3]);print(I[m[0]-1].strip()[:200] if m else I[5].strip()[:200])
import json
c={'format':'clm-context/v1','entries':[{'id':'note1','role':'note','body':'Stage1: deploy quotes-api 7.20.4-0a00 at stage-1/deploy/deploys.log:4. Release notes stage-1/deploy/release-notes-7.20.4-0a00.md:8 rates-svc timeout_ms 2500->600; :16 db pool 48->12. Logs: 95 rates-svc timeouts (dominant), 7 db pool waits (first stage-1/logs/quotes-api.log:150). Hypothesis CLIENT_TIMEOUT_TOO_LOW value 600. Next: advance.'}]}
json.dump(c,open('/task/workspace/context.json','w'))