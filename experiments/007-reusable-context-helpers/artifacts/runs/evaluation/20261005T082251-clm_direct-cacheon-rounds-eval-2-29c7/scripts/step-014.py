import re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read())
import os
for f in sorted(os.listdir(b+'logs')):
    for i,l in enumerate(open(b+'logs/'+f),1):
        if not re.search(r'request ok|heartbeat|gc |health ok|slow query|heap',l):
            print(f,i,l.strip()[:150])