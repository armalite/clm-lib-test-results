import json,re
t=open('/task/workspace/spill/s5.obs.txt').read()
ls=[l[:150] for l in t.split('\n') if re.search(r'§|==|version',l)]
o='\n'.join(ls);i=o.find('== 26');print(o[i:i+5000] if i>=0 else o[-5000:])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
json.dump(c,open('/task/workspace/context.json','w'))