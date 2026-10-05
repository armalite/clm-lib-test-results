import os,re
open('/task/workspace/notes.md','a').write('\nR8: board B cause MEMORY_LEAK (round-08/board.md:3); C ongoing restarting (round-08/board.md:4); VENDOR_TICKET closed (round-08/board.md:5). Log format now JSON.\n')
d='/task/fixtures/round-08/logs/'
for f in sorted(os.listdir(d)):
  for i,l in enumerate(open(d+f),1):
    if '"INFO"' not in l: print(f,i,l.strip()[:150])
