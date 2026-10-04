import json,re
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1: release notes stage-1/deploy/release-notes-8.19.0-ff7b.md:9 risk-score timeout 2500->800; :15 db.pool.max_size 60->14. deploy stage-1/deploy/deploys.log:4 quotes-api 8.19.0-ff7b 08:21:06. config yaml:11 pool 60, :7 timeout 2500. gateway 503 upstream timeout from line 93 on. quotes-api.log:206 first ERROR risk-score timed out after 800ms (95 such errors). oncall suspects risk-score timeout (informal).'}]}
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/stage-1/logs/quotes-api.log'
n=0
for i,l in enumerate(open(b),1):
  if re.search('pool|risk-score.*ms',l,re.I) and 'timed out' not in l:
    n+=1
    if n<8:print(i,l.strip()[:160])
print(n)