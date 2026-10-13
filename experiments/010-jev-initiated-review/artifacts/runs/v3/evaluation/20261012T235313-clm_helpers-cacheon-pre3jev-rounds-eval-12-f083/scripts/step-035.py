import json
print(open('/task/workspace/spill/s33.obs.txt').read()[:3000])
c=json.load(open('/task/workspace/context.json'))
n1=[e for e in c['entries'] if e['id']=='n1'][0]
n1['body']+=" Round8 released; raw grep output in /task/workspace/spill/s33.obs.txt (board.md 5 lines; Jev flagged board r8 relevant to n1)."
c['entries']=[n1]
json.dump(c,open('/task/workspace/context.json','w'))