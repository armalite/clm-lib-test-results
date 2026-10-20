# Exposure report (p015-exposure/1): dev-v3a

| | dev-v3a.s01-docthread-dev-1-paper_clm_shell.r1 |
| --- | --- |
| arm (version) | paper_clm_shell (paper-clm-shell/3) |
| outcome | arm_failure |
| turns planned / attempted / completed | 8 / 4 / 3 |
| score (points / recall) | 4/10, 0/3 |
| main / summariser logical calls | 19 / 0 |
| attempts (retries, failed, refused, truncated) | 19 (0, 0, 0, 0) |
| peak reported main input (tokens) | 31,727 |
| peak estimated request (tokens) | 31,138 |
| input / cache read / cache write / output (tokens) | 399,514 / 359,947 / 39,529 / 7,687 |
| notices | over_limit 1, reminder 1, rollback 6 |
| context management | edits_accepted 0, edits_rejected 1, commands 8, command_output_bytes 25,646, rollback_events 6, rollbacks 6, carried_rejections 0, over_limit_requests 1, held_outputs n/a, summaries n/a, context_limit_records 1 |
| task-tool calls / delivered chars / repeated | 19 / 44,753 / 0 |
| provider time / wall time (s) | 100.7 / 118.0 |
| cost confirmed / assumed (USD) | 0.247759 / 0 |

## dev-v3a.s01-docthread-dev-1-paper_clm_shell.r1: per turn

| turn | ending | attempts main / summary | retries | peak reported input (tokens) | cost (USD) | notices | tool calls | tool chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | completed | 6 / 0 | 0 | 18,447 | 0.068389 | none | 10 | 29,929 |
| 2 | completed | 2 / 0 | 0 | 20,154 | 0.017895 | none | 7 | 1,942 |
| 3 | completed | 1 / 0 | 0 | 20,500 | 0.005559 | none | 0 | 0 |
| 4 | context_limit | 10 / 0 | 0 | 31,727 | 0.155916 | over_limit 1, reminder 1, rollback 6 | 2 | 12,882 |
