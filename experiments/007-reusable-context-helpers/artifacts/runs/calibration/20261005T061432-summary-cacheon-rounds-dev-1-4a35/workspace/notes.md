R1: only slow query noise, board empty, CHG-108 PROPOSED (search HPA) not applied.

R2: follow-ups OPEN ALERT_TUNING(b:3),RUNBOOK_UPDATE(b:4),VENDOR_TICKET(b:5). CHG-120 APPLIED notify-worker max_inflight=0 (changes.md:4). auth-svc db pool exhausted lines 1,3,15,22,23,25,44,65,69.

R3: Thread A opened DB_POOL_EXHAUSTED auth-svc+search-api ongoing (round-03/board.md:3). Logs auth-svc.log:7-19, search-api.log:1-14. CHG-125 dashboards irrelevant.

R4: Thread B opened payments-svc suspected CACHE_STAMPEDE ongoing (round-04/board.md:3). But logs show 429 upstream=fx-rates in payments-svc.log:1,3,7,25,31,45 and checkout-api.log:9,19,50,53,59,62 -> likely UPSTREAM_RATE_LIMIT. auth/search pool exhausted continues (auth 7-39, search 4-30). CHG-133 TLS tickets irrelevant?

R5: Thread A mitigated (round-05/board.md:3), CHG-143 mitigation auth-svc (round-05/changes.md:4); no pool errors in R5 logs. Thread B adds checkout-api (round-05/board.md:4), still CACHE_STAMPEDE per board but logs 429 fx-rates checkout-api.log:21-65, payments-svc.log:13-73. Follow-up OPEN CAPACITY_REVIEW (round-05/board.md:5).

R6 raw:
board.md 3 - Follow-up CLOSED ALERT_TUNING.
board.md 4 - Follow-up OPEN CUSTOMER_COMMS: customer communication about the impact.
changes.md 3 - CHG-147 APPLIED: retry budget for idempotent GETs set to 1
checkout-api.log 19-77 6 upstream returned N upstream=fx-rates retry_after_s=N
payments-svc.log 3-76 11 upstream returned N upstream=fx-rates retry_after_s=N

R7 raw:
checkout-api.log 11-66 12 upstream returned N upstream=fx-rates retry_after_s=N
payments-svc.log 1-82 10 upstream returned N upstream=fx-rates retry_after_s=N

R8 raw:
board.md 3 - Thread A status: resolved (no recurrence for two hours).
board.md 4 - Thread B root cause revised: an upstream provider rejecting requests with 429 (UPSTREAM_RATE_LIMIT); this supersedes the earlier suspicion of CACHE_STAMPEDE.
board.md 5 - Thread C opened: request failures on some notify-worker pods; cause not yet identified. Status: ongoing.
changes.md 3 - CHG-159 PROPOSED: move batch jobs to off-peak window (not applied)
checkout-api.log 1-54 9 N","upstream":"fx-rates","retry_after_s":N}
notify-worker.log 5-72 6 failed","key":"http.max_inflight","value":"N","build":"N.N.N"}
payments-svc.log 2-83 13 N","upstream":"fx-rates","retry_after_s":N}

R8: A resolved (round-08/board.md:3). B cause UPSTREAM_RATE_LIMIT (round-08/board.md:4). Thread C notify-worker ongoing (round-08/board.md:5), logs round-08/logs/notify-worker.log:5-72 max_inflight=0 -> BAD_CONFIG_ROLLOUT via CHG-120. B refs round-08/logs/payments-svc.log:2-83 (wide), checkout-api.log:1-54.

R9 raw:
board.md 3 - Thread B status: mitigated (workaround in place; permanent fix pending).
board.md 4 - Thread C note: failing pods still restarting; investigation continues.
changes.md 3 - CHG-164 APPLIED: retry budget for idempotent GETs set to 1
checkout-api.log 34-55 2 N","upstream":"fx-rates","retry_after_s":N}
notify-worker.log 3-67 9 failed","key":"http.max_inflight","value":"N","build":"N.N.N"}
payments-svc.log 34-42 2 N","upstream":"fx-rates","retry_after_s":N}

R10 raw:
board.md 3 - Follow-up CLOSED CAPACITY_REVIEW.
changes.md 3 - CHG-171 APPLIED: retry budget for idempotent GETs set to 1
checkout-api.log [6, 11] "msg":"upstream returned N","upstream":"fx-rates","retry_after_s":N}
notify-worker.log [16, 21, 27, 30, 50, 70, 72, 81, 82] "msg":"config validation failed","key":"http.max_inflight","value":"N","build":"N.N.N"}
payments-svc.log [56, 72] "msg":"upstream returned N","upstream":"fx-rates","retry_after_s":N}
