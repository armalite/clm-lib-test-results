import json
p='/task/workspace/context.json'
c=json.load(open(p))
n=c['entries'][0]['body']+"\nR7: board round-07/board.md:3 Thread B cause revised DISK_PRESSURE (shipping+notify); :4 Thread D false alarm; :5 POSTMORTEM_DRAFT CLOSED. changes.md:3 CHG-149 PROPOSED only. R7 logs grep: no ERROR/fail hits (disk WARNs not grepped; recheck disk lines R7 for refs)."
c['entries']=[{'id':'n1','role':'note','body':n}]
json.dump(c,open(p,'w'))
print('ok')