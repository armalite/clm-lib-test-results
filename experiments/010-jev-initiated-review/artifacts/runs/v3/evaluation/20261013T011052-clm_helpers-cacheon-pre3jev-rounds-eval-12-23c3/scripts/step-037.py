import json,re
t=open('/task/workspace/spill/s35.obs.txt').read()
ls=[l for l in t.splitlines() if l.startswith(('board','changes'))]
print('\n'.join(ls))
err=[l for l in t.splitlines() if not l.startswith(('board','changes'))]
import collections
c=collections.Counter(l.split(' ')[0] for l in err)
print(c)
for l in err[:1]+[x for x in err if 'pricing' in x][:2]+[x for x in err if 'ledger' in x][:2]:print(l[:140])
ctx=json.load(open('/task/workspace/context.json'))
st=[e for e in ctx['entries'] if e['id']=='st8'][0]
st['body']+=' R9 board/changes: '+' | '.join(ls)[:1500]
ctx['entries']=[st]
json.dump(ctx,open('/task/workspace/context.json','w'))