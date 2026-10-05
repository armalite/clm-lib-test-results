R1: board empty; only slow query WARNs in all logs (noise).

R2: board.md:3-5 follow-ups OPEN ALERT_TUNING, RUNBOOK_UPDATE, VENDOR_TICKET. changes.md:4 CHG-120 APPLIED notify-worker http.max_inflight=0 (possible BAD_CONFIG); changes.md:5 CHG-121 payments no config. auth-svc db pool exhausted WARNs at lines 1,3,15,22,23,25 + 3 more (9 total); no board thread yet. Other services: only noise.

R2 auth-svc db pool exhausted also at lines 44,65,69 (in_use grows 12->20). Notify-worker R2 log shows only INFO lines (gaps at 5,7,17-19,33,39,42,45,50,53,56 not checked).

R3: board.md:3 Thread A DB_POOL_EXHAUSTED auth-svc+search-api ongoing. auth-svc.log:7-19 pool exhausted; search-api.log:1-14. changes CHG-125 dashboards only.
