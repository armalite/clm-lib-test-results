import json,re,glob
d=json.load(open('/task/workspace/context.json'))
n=[x for x in d['entries'] if x['id']=='n1'][0]
n['body']=n['body'].replace(' NEXT: advance to R9.','')+' R9: board.md:3 Thread B +checkout-api; :4 Thread B mitigated; :5 Thread C pods restarting ongoing; :6 Thread D false alarm (drop MEMORY_LEAK); :7 CLOSED DATA_BACKFILL.'
d['entries']=[n]
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  L=open(f).read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search(r'disk|batch_size|429|heap|ERROR',l,re.I)]
  print(f.split('/')[-1],len(h),h[:1],h[-1:] ,L[h[0]-1][:150] if h else '')
n['body']+=' R9 logs: see step26 obs.'
json.dump(d,open('/task/workspace/context.json','w'))