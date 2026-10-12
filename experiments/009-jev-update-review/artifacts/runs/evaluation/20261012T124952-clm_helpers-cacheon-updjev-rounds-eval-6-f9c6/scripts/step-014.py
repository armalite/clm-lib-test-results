import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
    L=open(f).read().splitlines();h=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|WARN',l)]
    s=set(re.sub(r'\d+','#',L[i-1].split(' ',3)[-1])[:90] for i in h)
    print(f.split('/')[-1],len(h),h[:1],h[-1:] if h else '',list(s)[:4])
d=json.load(open('/task/workspace/context.json'))
n=[x for x in d['entries'] if x['id']=='n1'][0]
n['body']+=' R5: board.md:3 OPEN VENDOR_TICKET.'
d['entries']=[n]
json.dump(d,open('/task/workspace/context.json','w'))