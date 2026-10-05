L=open('/task/fixtures/round-08/logs/search-api.log').read().splitlines()
for i,l in enumerate(L):
    if 'config validation' in l: print(i+1,l[:200]);break
open('/task/workspace/notes.md','a').write('\nR8: board.md:3 A resolved; :4 B mitigated; :5 Thread C search-api failures ongoing cause unknown; :6 DATA_BACKFILL OPEN; :7 VENDOR_TICKET CLOSED. search-api.log 429 x6 (1-66), config validation failed x9 (2-72) -> likely BAD_CONFIG_ROLLOUT CHG-120 round-02/changes.md:3. auth tls 8-61, shipping tls 50-60.\n')
