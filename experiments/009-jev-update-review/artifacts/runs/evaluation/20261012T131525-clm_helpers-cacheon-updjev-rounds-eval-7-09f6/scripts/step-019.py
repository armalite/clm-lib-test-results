import json,re,glob
print(open('/task/fixtures/round-07/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  L=open(f).read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search(r'429|disk|pool|cache|miss|error|ERROR',l)]
  print(f.split('/')[-1],len(h),h[:12])
  if h: print(' ',L[h[0]-1][:160])
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]['body'].replace(' Next: advance to R7.','')
n+=' R7: CHG-154 PROPOSED HPA (irrelevant).'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open('/task/workspace/context.json','w'))