import os,re,json
r='/task/fixtures/round-02/'
for i,l in enumerate(open(r+'board.md'),1):print('board',i,l.rstrip())
d=r+'logs/'
for f in sorted(os.listdir(d)):
  for i,l in enumerate(open(d+f),1):
    if 'slow query' not in l and re.search(r'ERROR|WARN|FATAL|error',l):print(f,i,l.strip()[:140])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':open('notes.md').read()}]},open('context.json','w'))