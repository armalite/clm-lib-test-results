import json,re,glob
b=open('/task/fixtures/round-09/board.md').read().splitlines()
for i,l in enumerate(b,1):print(i,l)
out=''
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  s=f.split('/')[-1][:-4];ln=[i for i,l in enumerate(open(f),1) if re.search('ERR|error|429|SERVFAIL|fail',l,re.I)]
  ms=set(re.sub(r'[0-9]+','#',l)[:90] for i,l in enumerate(open(f),1) if i in ln[:3])
  out+=f'{s} n={len(ln)} {ln[:1]}-{ln[-1:]} ;'
  print(s,len(ln),ms)
n=open('notes.md').read()+'R9: '+out+' board see next obs\n'
open('notes.md','w').write(n)
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('context.json','w'))