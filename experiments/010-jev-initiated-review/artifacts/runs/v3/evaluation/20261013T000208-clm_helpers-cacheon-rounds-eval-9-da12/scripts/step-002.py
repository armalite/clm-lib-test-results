import json
open('/task/workspace/cm.py','w').write('''import json
P="/task/workspace/context.json"
def setnotes(text):
    json.dump({"format":"clm-context/v1","entries":[{"id":"notes","role":"note","body":text}]},open(P,"w"))
''')
import sys;sys.path.insert(0,'/task/workspace')
import cm
cm.setnotes('NOTES: R1: board empty; changes.md:3 CHG-108 APPLIED TLS session ticket rotation hourly. Logs (notify-worker, shipping-svc, ledger-svc, inventory-svc, search-api) only routine slow-query WARNs (noise). No incidents yet. Helper: cm.setnotes(text) rewrites context to single note.')
print('ok')