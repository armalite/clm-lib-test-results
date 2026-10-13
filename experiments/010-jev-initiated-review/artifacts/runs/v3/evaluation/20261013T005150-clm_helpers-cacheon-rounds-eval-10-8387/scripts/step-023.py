import json
n=open('notes.md').read()+'R8 board: A resolved (round-08/board.md:3); B mitigated (:4); CHG-157 PROPOSED irrelevant.\n'
open('notes.md','w').write(n)
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n+'NEXT: advance to R9.'}]},open('context.json','w'))