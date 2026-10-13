import sys; sys.path.insert(0, '/task/fixtures')
from handbook_tools import search, show
import glob
for f in sorted(glob.glob('/task/fixtures/handbook/*.md')):
    print(f[-8:], open(f).readline().strip()[:150])
