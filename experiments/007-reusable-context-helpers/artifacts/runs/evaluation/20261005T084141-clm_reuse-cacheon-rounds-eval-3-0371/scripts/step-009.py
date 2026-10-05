import ctx
c=ctx.load()
notes=[e['body'] for e in c['entries'] if e['role']=='note']
notes.append('R3: board empty (no change). CHG-125 APPLIED retry budget=1 (benign). cert errors continue inventory-svc.log:9-18,39-57,71; ledger-svc.log:23-43,61-69. No search-api errors. Next: advance to R4.')
ctx.reset(notes)
print('ok')