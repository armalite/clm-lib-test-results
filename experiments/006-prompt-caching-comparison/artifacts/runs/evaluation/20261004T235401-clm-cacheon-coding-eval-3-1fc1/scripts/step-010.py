print(open('/task/workspace/invoice/core.py').read()[:3000])
import glob
for f in sorted(glob.glob('/task/fixtures/stage-*/REQUIREMENTS.md')):print(f);print(open(f).read()[:1200])