import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|FATAL|WARN',l) and 'slow' not in l: print(f.split('/')[-1],i,l.strip()[:150])
print(open('/task/fixtures/round-02/board.md').read())
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty, no incident; background slow-query WARNs only. CHG-108 PROPOSED. R2: board follow-ups OPEN ALERT_TUNING(board.md:3), RUNBOOK_UPDATE(:4), VENDOR_TICKET(:5). changes R2: CHG-120 APPLIED notify-worker 8.56.0 sets http.max_inflight=0 (round-02/changes.md:4) -> suspect BAD_CONFIG_ROLLOUT; CHG-121 payments no config.'}]}
json.dump(c,open('/task/workspace/context.json','w'))