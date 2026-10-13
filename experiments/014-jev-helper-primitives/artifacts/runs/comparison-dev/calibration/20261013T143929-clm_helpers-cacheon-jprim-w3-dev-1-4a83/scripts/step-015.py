p='/task/workspace/exporter/core.py'
s=open(p).read()
import re
print([l for l in s.splitlines() if 'max_records' in l or 'exported_by' in l])
s=s.replace("    res = {'exported_by': user.get('name')}","    res = {}\n    if user.get('role') != 'admin':\n        res['exported_by'] = user.get('name')")
open(p,'w').write(s)
print('\n'.join(l for l in s.splitlines() if 'max' in l))