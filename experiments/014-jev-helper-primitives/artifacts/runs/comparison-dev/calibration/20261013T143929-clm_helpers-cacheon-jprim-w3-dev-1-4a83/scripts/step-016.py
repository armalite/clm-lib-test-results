p='/task/workspace/exporter/core.py'
s=open(p).read()
L=s.splitlines()
i=[k for k,l in enumerate(L) if "mr = params.get('max_records')" in l][0]
print('\n'.join(L[i:i+6]))