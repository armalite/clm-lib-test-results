import sys;sys.path.insert(0,'/task/workspace')
import h,json
print(open('/task/fixtures/round-07/board.md').read())
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]['body'].replace(' Next: advance R7, scan(7).',' R7: 429s continue checkout-api.log:11-29,56-66, payments-svc.log:1-36,71-82; board R7 see next obs.')
h.setctx([{'id':'n1','role':'note','body':n}])