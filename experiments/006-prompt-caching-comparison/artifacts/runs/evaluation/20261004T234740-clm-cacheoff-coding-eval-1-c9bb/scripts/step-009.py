import os
for n in range(1,5):
    p=f'/task/fixtures/stage-{n}/REQUIREMENTS.md'
    print(n,os.path.exists(p))
print(open('/task/fixtures/stage-4/REQUIREMENTS.md').read()[:2500])
print(open('/task/workspace/invoice/core.py').read()[:3000])