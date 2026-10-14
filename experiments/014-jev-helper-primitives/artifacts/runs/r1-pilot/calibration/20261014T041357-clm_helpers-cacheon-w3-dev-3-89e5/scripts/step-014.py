import re
for i,l in enumerate(open('/task/workspace/exporter/core.py').read().split('\n'),1):
    if 'exported_by' in l or 'max_records' in l or 'doc' in l: print(i,l)