import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|FATAL|429|max_inflight|pool|OOM|cert|DNS|lag|disk',l,re.I) and 'slow' not in l:
            print(f.split('/')[-1],i,l.strip()[:150])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; CHG-108 PROPOSED (ignore). Background slow-query WARNs = noise in all 5 svcs. R2: board.md:3-5 follow-ups OPEN ALERT_TUNING,RUNBOOK_UPDATE,VENDOR_TICKET. changes.md:4 CHG-120 APPLIED notify-worker 8.56.0 sets http.max_inflight=0 (suspect BAD_CONFIG); :5 CHG-121 payments 8.56.0 no cfg; :3 CHG-116 log sampling.'}]}
json.dump(c,open('/task/workspace/context.json','w'))