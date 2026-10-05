from ctx import keep_notes
import json,re
n=json.load(open('context.json'))['entries'][0]['body']
L=[(i+1,l.strip()[:160]) for i,l in enumerate(open('/task/fixtures/round-08/logs/search-api.log')) if re.search(r'ERROR',l) and '429' not in l]
print(L[:5],len(L))
keep_notes(n+'\nR8: board.md:3 A resolved; :4 B mitigated; :5 Thread C search-api failures cause unknown ongoing; :6 OPEN DATA_BACKFILL; :7 CLOSED VENDOR_TICKET. auth-svc.log:8-61, shipping-svc.log:50-60 cert errs (2 each, dropping); search-api.log:1-72 429 tax-provider (15).')