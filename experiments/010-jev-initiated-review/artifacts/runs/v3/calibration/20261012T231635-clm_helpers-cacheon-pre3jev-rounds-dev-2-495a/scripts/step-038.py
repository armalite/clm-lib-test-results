import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
b=n['body'].replace('R9 released; round-09 board/changes/search-api scan output in spill/s34.obs.txt (re-read if needed).','R9: board.md:3 Thread C pods restarting; changes.md:3 CHG-166 APPLIED retry budget. search-api round-09/logs/search-api.log:2 config validation failed http.max_inflight=-1 (lines 2-62 repeated) => Thread C likely BAD_CONFIG_ROLLOUT from CHG-120 (round-02/changes.md:3); 429s from tax-provider continue (Thread D). Next: advance to R10.')
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':b}]},open('/task/workspace/context.json','w'))
print('ok')