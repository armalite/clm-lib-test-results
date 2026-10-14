import json,subprocess,sys,reghelper
reghelper.update(6)
p='exporter/core.py';s=open(p).read()
import re
print([l for l in s.split('\n') if 'exported_by' in l or 'max_records' in l])
