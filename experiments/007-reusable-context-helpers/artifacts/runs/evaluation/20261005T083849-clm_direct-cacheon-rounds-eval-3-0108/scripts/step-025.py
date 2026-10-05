import json
n=open('/task/workspace/notes.txt').read()+'\nR8: board B cause revised MEMORY_LEAK (round-08/board.md:3); C still restarting (:4); FU CLOSED VENDOR_TICKET (:5). CHG-160 PROPOSED. search-api config errs round-08/logs/search-api.log:2-76; checkout no errors. Next: advance to r9.'
open('/task/workspace/notes.txt','w').write(n)
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))
print('ok')