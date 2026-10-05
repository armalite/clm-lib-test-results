import ctx
c=ctx.load()
notes=[e['body'] for e in c['entries'] if e['role']=='note']
notes.append('R7: board.md:3 Thread A RESOLVED. board.md:4 Thread C search-api failures ongoing -> logs show BAD_CONFIG_ROLLOUT http.max_inflight=-1 search-api.log:17-58 (traces to round-01/changes.md:4 CHG-113). board.md:5 Thread D DISK_PRESSURE false alarm. board.md:6 VENDOR_TICKET OPEN. checkout-api heap WARNs continue lines 6-67 (MEMORY_LEAK likely, board says rate limit). Next: advance to R8.')
ctx.reset(notes)
print('ok')