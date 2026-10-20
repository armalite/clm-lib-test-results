# Exposure report (p015-exposure/1): confirm1

| | confirm1.s01-docthread-confirm-1-guarded_clm.r1 | confirm1.s02-docthread-confirm-1-paper_clm_shell.r1 | confirm1.s03-docthread-confirm-1-token_tail_p015.r1 | confirm1.s04-docthread-confirm-2-paper_clm_shell.r1 | confirm1.s05-docthread-confirm-2-token_tail_p015.r1 | confirm1.s06-docthread-confirm-2-guarded_clm.r1 | confirm1.s07-docthread-confirm-3-token_tail_p015.r1 | confirm1.s08-docthread-confirm-3-guarded_clm.r1 | confirm1.s09-docthread-confirm-3-paper_clm_shell.r1 | confirm1.s10-docthread-confirm-4-guarded_clm.r1 | confirm1.s11-docthread-confirm-4-paper_clm_shell.r1 | confirm1.s12-docthread-confirm-4-token_tail_p015.r1 | confirm1.s13-docthread-confirm-5-paper_clm_shell.r1 | confirm1.s14-docthread-confirm-5-token_tail_p015.r1 | confirm1.s15-docthread-confirm-5-guarded_clm.r1 | confirm1.s16-docthread-confirm-6-token_tail_p015.r1 | confirm1.s17-docthread-confirm-6-guarded_clm.r1 | confirm1.s18-docthread-confirm-6-paper_clm_shell.r1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| arm (version) | guarded_clm (guarded-clm 0.2.0.dev1) | paper_clm_shell (paper-clm-shell/2) | token_tail_p015 (token-tail-p015/1) | paper_clm_shell (paper-clm-shell/2) | token_tail_p015 (token-tail-p015/1) | guarded_clm (guarded-clm 0.2.0.dev1) | token_tail_p015 (token-tail-p015/1) | guarded_clm (guarded-clm 0.2.0.dev1) | paper_clm_shell (paper-clm-shell/2) | guarded_clm (guarded-clm 0.2.0.dev1) | paper_clm_shell (paper-clm-shell/2) | token_tail_p015 (token-tail-p015/1) | paper_clm_shell (paper-clm-shell/2) | token_tail_p015 (token-tail-p015/1) | guarded_clm (guarded-clm 0.2.0.dev1) | token_tail_p015 (token-tail-p015/1) | guarded_clm (guarded-clm 0.2.0.dev1) | paper_clm_shell (paper-clm-shell/2) |
| outcome | complete | arm_failure | complete | arm_failure | complete | complete | complete | complete | arm_failure | complete | arm_failure | complete | arm_failure | complete | complete | complete | complete | arm_failure |
| turns planned / attempted / completed | 8 / 8 / 8 | 8 / 4 / 3 | 8 / 8 / 8 | 8 / 1 / 0 | 8 / 8 / 8 | 8 / 8 / 8 | 8 / 8 / 8 | 8 / 8 / 8 | 8 / 4 / 3 | 8 / 8 / 8 | 8 / 4 / 3 | 8 / 8 / 8 | 8 / 4 / 3 | 8 / 8 / 8 | 8 / 8 / 8 | 8 / 8 / 8 | 8 / 8 / 8 | 8 / 4 / 3 |
| score (points / recall) | 10/10, 3/3 | 4/10, 0/3 | 10/10, 3/3 | 0/10, 0/3 | 10/10, 3/3 | 10/10, 3/3 | 10/10, 3/3 | 10/10, 3/3 | 4/10, 0/3 | 9/10, 3/3 | 4/10, 0/3 | 9/10, 3/3 | 4/10, 0/3 | 10/10, 3/3 | 10/10, 3/3 | 10/10, 3/3 | 9/10, 3/3 | 4/10, 0/3 |
| main / summariser logical calls | 28 / 0 | 21 / 0 | 29 / 4 | 16 / 0 | 28 / 4 | 37 / 0 | 19 / 2 | 26 / 0 | 20 / 0 | 31 / 0 | 23 / 0 | 34 / 5 | 23 / 0 | 25 / 4 | 26 / 0 | 17 / 1 | 28 / 0 | 22 / 0 |
| attempts (retries, failed, refused, truncated) | 28 (0, 0, 0, 0) | 21 (0, 0, 0, 0) | 33 (0, 0, 0, 0) | 16 (0, 0, 0, 0) | 32 (0, 0, 0, 0) | 37 (0, 0, 0, 0) | 21 (0, 0, 0, 0) | 26 (0, 0, 0, 0) | 20 (0, 0, 0, 0) | 31 (0, 0, 0, 0) | 23 (0, 0, 0, 0) | 39 (0, 0, 0, 0) | 23 (0, 0, 0, 0) | 29 (0, 0, 0, 0) | 26 (0, 0, 0, 0) | 18 (0, 0, 0, 0) | 28 (0, 0, 0, 0) | 22 (0, 0, 0, 0) |
| peak reported main input (tokens) | 26,908 | 30,230 | 22,593 | 29,697 | 23,165 | 26,684 | 21,669 | 28,122 | 29,995 | 27,796 | 30,862 | 21,136 | 32,126 | 21,752 | 25,548 | 20,160 | 26,583 | 30,089 |
| peak estimated request (tokens) | 27,014 | 30,603 | 22,385 | 30,341 | 21,335 | 26,918 | 22,379 | 28,215 | 30,465 | 27,954 | 31,249 | 21,359 | 31,621 | 21,101 | 25,726 | 21,297 | 26,888 | 30,654 |
| input / cache read / cache write / output (tokens) | 376,422 / 62,100 / 314,294 / 12,816 | 452,336 / 421,604 / 30,690 / 9,988 | 461,517 / 288,994 / 172,457 / 11,649 | 337,208 / 292,677 / 44,499 / 5,352 | 382,662 / 221,706 / 160,892 / 11,772 | 589,930 / 82,368 / 507,525 / 15,913 | 331,202 / 251,336 / 79,824 / 7,287 | 425,459 / 57,350 / 368,083 / 11,331 | 425,935 / 391,963 / 33,932 / 7,604 | 444,116 / 68,850 / 375,235 / 18,156 | 485,756 / 451,261 / 34,449 / 6,981 | 489,520 / 287,249 / 202,193 / 14,753 | 496,605 / 462,241 / 34,318 / 10,037 | 309,262 / 150,653 / 158,551 / 11,401 | 431,036 / 57,375 / 373,635 / 9,888 | 235,734 / 184,891 / 50,807 / 5,180 | 343,723 / 61,938 / 281,757 / 9,360 | 487,038 / 454,764 / 32,230 / 8,916 |
| notices | pressure 5 | over_limit 1, reminder 1, rollback 6, rollback_feedback 2 | none | over_limit 1, reminder 1, rollback 6, rollback_feedback 2 | none | pressure 7 | none | pressure 6 | over_limit 1, reminder 1, rollback 6, rollback_feedback 2 | pressure 5 | over_limit 1, reminder 1, rollback 6 | none | over_limit 1, reminder 1, rollback 6 | none | pressure 3 | none | pressure 3 | over_limit 1, reminder 1, rollback 6, rollback_feedback 1 |
| context management | edits_accepted 3, edits_rejected 1, edits_unchanged 0, protected_refused 0, held_outputs 2, held_output_refetches 1, over_limit_requests 0, rollbacks n/a, summaries n/a, context_limit_records 0 | edits_accepted 0, edits_rejected 2, commands 8, command_output_bytes 10,323, rollback_events 6, rollbacks 6, carried_rejections 2, over_limit_requests 1, held_outputs n/a, summaries n/a, context_limit_records 1 | pressure_triggers 4, summaries 4, summaries_too_large 0, summaries_empty 0, summary_cap_reached 0, edits_accepted n/a, held_outputs n/a, rollbacks n/a, context_limit_records 0 | edits_accepted 0, edits_rejected 2, commands 8, command_output_bytes 4,451, rollback_events 6, rollbacks 6, carried_rejections 2, over_limit_requests 1, held_outputs n/a, summaries n/a, context_limit_records 1 | pressure_triggers 4, summaries 4, summaries_too_large 0, summaries_empty 0, summary_cap_reached 0, edits_accepted n/a, held_outputs n/a, rollbacks n/a, context_limit_records 0 | edits_accepted 6, edits_rejected 1, edits_unchanged 0, protected_refused 1, held_outputs 7, held_output_refetches 6, over_limit_requests 0, rollbacks n/a, summaries n/a, context_limit_records 0 | pressure_triggers 2, summaries 2, summaries_too_large 0, summaries_empty 0, summary_cap_reached 0, edits_accepted n/a, held_outputs n/a, rollbacks n/a, context_limit_records 0 | edits_accepted 3, edits_rejected 1, edits_unchanged 0, protected_refused 1, held_outputs 3, held_output_refetches 3, over_limit_requests 0, rollbacks n/a, summaries n/a, context_limit_records 0 | edits_accepted 0, edits_rejected 3, commands 10, command_output_bytes 13,167, rollback_events 6, rollbacks 6, carried_rejections 2, over_limit_requests 1, held_outputs n/a, summaries n/a, context_limit_records 1 | edits_accepted 4, edits_rejected 0, edits_unchanged 0, protected_refused 0, held_outputs 4, held_output_refetches 3, over_limit_requests 0, rollbacks n/a, summaries n/a, context_limit_records 0 | edits_accepted 0, edits_rejected 1, commands 10, command_output_bytes 14,990, rollback_events 6, rollbacks 6, carried_rejections 0, over_limit_requests 1, held_outputs n/a, summaries n/a, context_limit_records 1 | pressure_triggers 5, summaries 5, summaries_too_large 0, summaries_empty 0, summary_cap_reached 0, edits_accepted n/a, held_outputs n/a, rollbacks n/a, context_limit_records 0 | edits_accepted 0, edits_rejected 2, commands 12, command_output_bytes 25,307, rollback_events 6, rollbacks 6, carried_rejections 0, over_limit_requests 1, held_outputs n/a, summaries n/a, context_limit_records 1 | pressure_triggers 4, summaries 4, summaries_too_large 0, summaries_empty 0, summary_cap_reached 0, edits_accepted n/a, held_outputs n/a, rollbacks n/a, context_limit_records 0 | edits_accepted 4, edits_rejected 0, edits_unchanged 0, protected_refused 0, held_outputs 1, held_output_refetches 0, over_limit_requests 0, rollbacks n/a, summaries n/a, context_limit_records 0 | pressure_triggers 1, summaries 1, summaries_too_large 0, summaries_empty 0, summary_cap_reached 0, edits_accepted n/a, held_outputs n/a, rollbacks n/a, context_limit_records 0 | edits_accepted 4, edits_rejected 0, edits_unchanged 0, protected_refused 0, held_outputs 3, held_output_refetches 2, over_limit_requests 0, rollbacks n/a, summaries n/a, context_limit_records 0 | edits_accepted 0, edits_rejected 2, commands 10, command_output_bytes 80,305, rollback_events 6, rollbacks 6, carried_rejections 1, over_limit_requests 1, held_outputs n/a, summaries n/a, context_limit_records 1 |
| task-tool calls / delivered chars / repeated | 37 / 130,981 / 8 | 22 / 62,998 / 0 | 36 / 129,878 / 8 | 13 / 48,459 / 0 | 38 / 136,873 / 7 | 48 / 207,010 / 18 | 25 / 61,366 / 1 | 35 / 124,941 / 4 | 19 / 45,517 / 0 | 41 / 166,164 / 10 | 21 / 44,990 / 0 | 44 / 174,587 / 13 | 20 / 51,255 / 0 | 38 / 136,775 / 10 | 31 / 103,089 / 8 | 22 / 46,544 / 0 | 39 / 147,475 / 8 | 21 / 57,585 / 0 |
| provider time / wall time (s) | 154.7 / 159.0 | 111.7 / 128.0 | 144.2 / 148.0 | 62.535 / 85 | 135.8 / 139.0 | 178.7 / 183.0 | 83.306 / 86 | 137.1 / 141.0 | 81.585 / 100.0 | 216.2 / 220.0 | 79.475 / 96 | 169.1 / 174.0 | 106.9 / 127.0 | 126.5 / 130.0 | 118.4 / 122.0 | 62.28 / 65 | 119.7 / 124.0 | 121.3 / 139.0 |
| cost confirmed / assumed (USD) | 0.926372 / 0 | 0.261006 / 0 | 0.605568 / 0 | 0.223366 / 0 | 0.564419 / 0 | 1.444495 / 0 | 0.32278 / 0 | 1.045039 / 0 | 0.239345 / 0 | 1.13348 / 0 | 0.246275 / 0 | 0.710619 / 0 | 0.278705 / 0 | 0.540632 / 0 | 1.044497 / 0 | 0.215868 / 0 | 0.810437 / 0 | 0.260775 / 0 |

## confirm1.s01-docthread-confirm-1-guarded_clm.r1: per turn

| turn | ending | attempts main / summary | retries | peak reported input (tokens) | cost (USD) | notices | tool calls | tool chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | completed | 6 / 0 | 0 | 18,290 | 0.144952 | none | 10 | 29,946 |
| 2 | completed | 2 / 0 | 0 | 19,905 | 0.098492 | none | 7 | 2,050 |
| 3 | completed | 1 / 0 | 0 | 20,520 | 0.0468 | none | 0 | 0 |
| 4 | completed | 11 / 0 | 0 | 26,908 | 0.520986 | pressure 5 | 15 | 96,181 |
| 5 | completed | 2 / 0 | 0 | 6,703 | 0.023824 | none | 1 | 457 |
| 6 | completed | 3 / 0 | 0 | 7,813 | 0.042238 | none | 3 | 1,589 |
| 7 | completed | 1 / 0 | 0 | 8,075 | 0.015577 | none | 0 | 0 |
| 8 | completed | 2 / 0 | 0 | 8,706 | 0.033503 | none | 1 | 758 |

## confirm1.s02-docthread-confirm-1-paper_clm_shell.r1: per turn

| turn | ending | attempts main / summary | retries | peak reported input (tokens) | cost (USD) | notices | tool calls | tool chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | completed | 6 / 0 | 0 | 18,267 | 0.068875 | none | 10 | 29,946 |
| 2 | completed | 2 / 0 | 0 | 20,088 | 0.022451 | none | 7 | 2,050 |
| 3 | completed | 1 / 0 | 0 | 20,884 | 0.006691 | none | 0 | 0 |
| 4 | context_limit | 12 / 0 | 0 | 30,230 | 0.162989 | over_limit 1, reminder 1, rollback 6, rollback_feedback 2 | 5 | 31,002 |

## confirm1.s03-docthread-confirm-1-token_tail_p015.r1: per turn

| turn | ending | attempts main / summary | retries | peak reported input (tokens) | cost (USD) | notices | tool calls | tool chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | completed | 7 / 0 | 0 | 21,126 | 0.078243 | none | 11 | 35,999 |
| 2 | completed | 2 / 1 | 0 | 21,364 | 0.084922 | none | 7 | 2,050 |
| 3 | completed | 1 / 0 | 0 | 8,683 | 0.003263 | none | 0 | 0 |
| 4 | completed | 13 / 3 | 0 | 22,593 | 0.398716 | none | 16 | 90,614 |
| 5 | completed | 2 / 0 | 0 | 10,765 | 0.025931 | none | 1 | 457 |
| 6 | completed | 1 / 0 | 0 | 11,008 | 0.003914 | none | 0 | 0 |
| 7 | completed | 1 / 0 | 0 | 11,269 | 0.003588 | none | 0 | 0 |
| 8 | completed | 2 / 0 | 0 | 11,814 | 0.006991 | none | 1 | 758 |

## confirm1.s04-docthread-confirm-2-paper_clm_shell.r1: per turn

| turn | ending | attempts main / summary | retries | peak reported input (tokens) | cost (USD) | notices | tool calls | tool chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | context_limit | 16 / 0 | 0 | 29,697 | 0.223366 | over_limit 1, reminder 1, rollback 6, rollback_feedback 2 | 13 | 48,459 |

## confirm1.s05-docthread-confirm-2-token_tail_p015.r1: per turn

| turn | ending | attempts main / summary | retries | peak reported input (tokens) | cost (USD) | notices | tool calls | tool chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | completed | 6 / 0 | 0 | 18,104 | 0.067104 | none | 10 | 30,279 |
| 2 | completed | 2 / 0 | 0 | 19,982 | 0.017665 | none | 7 | 2,314 |
| 3 | completed | 1 / 0 | 0 | 20,290 | 0.00546 | none | 0 | 0 |
| 4 | completed | 11 / 4 | 0 | 23,165 | 0.451137 | none | 16 | 101,442 |
| 5 | completed | 2 / 0 | 0 | 3,231 | 0.006455 | none | 1 | 476 |
| 6 | completed | 3 / 0 | 0 | 4,408 | 0.008764 | none | 3 | 1,600 |
| 7 | completed | 1 / 0 | 0 | 4,726 | 0.00304 | none | 0 | 0 |
| 8 | completed | 2 / 0 | 0 | 5,330 | 0.004794 | none | 1 | 762 |

## confirm1.s06-docthread-confirm-2-guarded_clm.r1: per turn

| turn | ending | attempts main / summary | retries | peak reported input (tokens) | cost (USD) | notices | tool calls | tool chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | completed | 6 / 0 | 0 | 21,801 | 0.166023 | none | 11 | 36,344 |
| 2 | completed | 3 / 0 | 0 | 23,540 | 0.147584 | pressure 1 | 7 | 2,314 |
| 3 | completed | 1 / 0 | 0 | 11,645 | 0.02487 | none | 0 | 0 |
| 4 | completed | 17 / 0 | 0 | 26,684 | 0.724055 | pressure 5 | 25 | 159,597 |
| 5 | completed | 2 / 0 | 0 | 17,571 | 0.079755 | none | 1 | 476 |
| 6 | completed | 3 / 0 | 0 | 18,366 | 0.123984 | none | 2 | 764 |
| 7 | completed | 3 / 0 | 0 | 22,422 | 0.129809 | pressure 1 | 1 | 6,753 |
| 8 | completed | 2 / 0 | 0 | 11,485 | 0.048415 | none | 1 | 762 |

## confirm1.s07-docthread-confirm-3-token_tail_p015.r1: per turn

| turn | ending | attempts main / summary | retries | peak reported input (tokens) | cost (USD) | notices | tool calls | tool chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | completed | 6 / 0 | 0 | 18,012 | 0.0698 | none | 10 | 29,770 |
| 2 | completed | 2 / 0 | 0 | 19,957 | 0.017543 | none | 7 | 2,441 |
| 3 | completed | 1 / 0 | 0 | 20,231 | 0.00529 | none | 0 | 0 |
| 4 | completed | 3 / 1 | 0 | 20,435 | 0.125311 | none | 4 | 26,805 |
| 5 | completed | 1 / 0 | 0 | 20,122 | 0.005661 | none | 0 | 0 |
| 6 | completed | 3 / 0 | 0 | 21,252 | 0.01718 | none | 3 | 1,590 |
| 7 | completed | 1 / 0 | 0 | 21,442 | 0.005559 | none | 0 | 0 |
| 8 | completed | 2 / 1 | 0 | 21,669 | 0.076436 | none | 1 | 760 |

## confirm1.s08-docthread-confirm-3-guarded_clm.r1: per turn

| turn | ending | attempts main / summary | retries | peak reported input (tokens) | cost (USD) | notices | tool calls | tool chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | completed | 4 / 0 | 0 | 14,704 | 0.073035 | none | 9 | 23,712 |
| 2 | completed | 2 / 0 | 0 | 16,580 | 0.080596 | none | 7 | 2,441 |
| 3 | completed | 1 / 0 | 0 | 17,349 | 0.038766 | none | 0 | 0 |
| 4 | completed | 10 / 0 | 0 | 28,122 | 0.505928 | pressure 4 | 15 | 96,438 |
| 5 | completed | 1 / 0 | 0 | 21,167 | 0.049001 | none | 0 | 0 |
| 6 | completed | 5 / 0 | 0 | 23,026 | 0.235816 | pressure 2 | 3 | 1,590 |
| 7 | completed | 1 / 0 | 0 | 9,796 | 0.019983 | none | 0 | 0 |
| 8 | completed | 2 / 0 | 0 | 10,380 | 0.041914 | none | 1 | 760 |

## confirm1.s09-docthread-confirm-3-paper_clm_shell.r1: per turn

| turn | ending | attempts main / summary | retries | peak reported input (tokens) | cost (USD) | notices | tool calls | tool chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | completed | 6 / 0 | 0 | 18,476 | 0.072497 | none | 10 | 29,770 |
| 2 | completed | 2 / 0 | 0 | 20,470 | 0.017695 | none | 7 | 2,441 |
| 3 | completed | 1 / 0 | 0 | 20,741 | 0.005405 | none | 0 | 0 |
| 4 | context_limit | 11 / 0 | 0 | 29,995 | 0.143748 | over_limit 1, reminder 1, rollback 6, rollback_feedback 2 | 2 | 13,306 |

## confirm1.s10-docthread-confirm-4-guarded_clm.r1: per turn

| turn | ending | attempts main / summary | retries | peak reported input (tokens) | cost (USD) | notices | tool calls | tool chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | completed | 5 / 0 | 0 | 14,914 | 0.098956 | none | 9 | 23,889 |
| 2 | completed | 2 / 0 | 0 | 16,599 | 0.079943 | none | 7 | 2,203 |
| 3 | completed | 1 / 0 | 0 | 17,116 | 0.038491 | none | 0 | 0 |
| 4 | completed | 16 / 0 | 0 | 27,796 | 0.761885 | pressure 5 | 21 | 131,714 |
| 5 | completed | 1 / 0 | 0 | 8,541 | 0.017633 | none | 0 | 0 |
| 6 | completed | 3 / 0 | 0 | 9,651 | 0.055487 | none | 3 | 1,589 |
| 7 | completed | 2 / 0 | 0 | 13,457 | 0.051186 | none | 1 | 6,769 |
| 8 | completed | 1 / 0 | 0 | 13,699 | 0.029899 | none | 0 | 0 |

## confirm1.s11-docthread-confirm-4-paper_clm_shell.r1: per turn

| turn | ending | attempts main / summary | retries | peak reported input (tokens) | cost (USD) | notices | tool calls | tool chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | completed | 5 / 0 | 0 | 14,748 | 0.052942 | none | 9 | 23,889 |
| 2 | completed | 2 / 0 | 0 | 16,513 | 0.01595 | none | 7 | 2,203 |
| 3 | completed | 1 / 0 | 0 | 16,817 | 0.004726 | none | 0 | 0 |
| 4 | context_limit | 15 / 0 | 0 | 30,862 | 0.172657 | over_limit 1, reminder 1, rollback 6 | 5 | 18,898 |

## confirm1.s12-docthread-confirm-4-token_tail_p015.r1: per turn

| turn | ending | attempts main / summary | retries | peak reported input (tokens) | cost (USD) | notices | tool calls | tool chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | completed | 6 / 0 | 0 | 17,918 | 0.066788 | none | 10 | 29,923 |
| 2 | completed | 2 / 0 | 0 | 19,696 | 0.017078 | none | 7 | 2,203 |
| 3 | completed | 1 / 0 | 0 | 20,012 | 0.005393 | none | 0 | 0 |
| 4 | completed | 17 / 5 | 0 | 21,136 | 0.600991 | none | 22 | 139,649 |
| 5 | completed | 2 / 0 | 0 | 3,271 | 0.006314 | none | 1 | 467 |
| 6 | completed | 3 / 0 | 0 | 4,393 | 0.007036 | none | 3 | 1,589 |
| 7 | completed | 1 / 0 | 0 | 4,584 | 0.00259 | none | 0 | 0 |
| 8 | completed | 2 / 0 | 0 | 5,178 | 0.004429 | none | 1 | 756 |

## confirm1.s13-docthread-confirm-5-paper_clm_shell.r1: per turn

| turn | ending | attempts main / summary | retries | peak reported input (tokens) | cost (USD) | notices | tool calls | tool chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | completed | 6 / 0 | 0 | 18,317 | 0.067427 | none | 10 | 30,184 |
| 2 | completed | 2 / 0 | 0 | 20,198 | 0.020128 | none | 7 | 2,323 |
| 3 | completed | 1 / 0 | 0 | 20,743 | 0.006126 | none | 0 | 0 |
| 4 | context_limit | 14 / 0 | 0 | 32,126 | 0.185024 | over_limit 1, reminder 1, rollback 6 | 3 | 18,748 |

## confirm1.s14-docthread-confirm-5-token_tail_p015.r1: per turn

| turn | ending | attempts main / summary | retries | peak reported input (tokens) | cost (USD) | notices | tool calls | tool chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | completed | 5 / 0 | 0 | 21,478 | 0.076646 | none | 11 | 35,712 |
| 2 | completed | 2 / 1 | 0 | 21,752 | 0.086789 | none | 7 | 2,323 |
| 3 | completed | 1 / 0 | 0 | 5,431 | 0.002504 | none | 0 | 0 |
| 4 | completed | 9 / 3 | 0 | 19,650 | 0.350858 | none | 15 | 95,917 |
| 5 | completed | 2 / 0 | 0 | 3,416 | 0.007292 | none | 1 | 461 |
| 6 | completed | 3 / 0 | 0 | 4,587 | 0.008867 | none | 3 | 1,600 |
| 7 | completed | 1 / 0 | 0 | 4,905 | 0.003086 | none | 0 | 0 |
| 8 | completed | 2 / 0 | 0 | 5,511 | 0.00459 | none | 1 | 762 |

## confirm1.s15-docthread-confirm-5-guarded_clm.r1: per turn

| turn | ending | attempts main / summary | retries | peak reported input (tokens) | cost (USD) | notices | tool calls | tool chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | completed | 5 / 0 | 0 | 21,521 | 0.124812 | none | 11 | 35,712 |
| 2 | completed | 3 / 0 | 0 | 23,306 | 0.13495 | pressure 1 | 7 | 2,323 |
| 3 | completed | 1 / 0 | 0 | 7,806 | 0.015336 | none | 0 | 0 |
| 4 | completed | 11 / 0 | 0 | 25,548 | 0.483007 | pressure 2 | 10 | 63,454 |
| 5 | completed | 1 / 0 | 0 | 19,724 | 0.045571 | none | 0 | 0 |
| 6 | completed | 3 / 0 | 0 | 20,937 | 0.141634 | none | 3 | 1,600 |
| 7 | completed | 1 / 0 | 0 | 21,316 | 0.049431 | none | 0 | 0 |
| 8 | completed | 1 / 0 | 0 | 21,614 | 0.049756 | none | 0 | 0 |

## confirm1.s16-docthread-confirm-6-token_tail_p015.r1: per turn

| turn | ending | attempts main / summary | retries | peak reported input (tokens) | cost (USD) | notices | tool calls | tool chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | completed | 6 / 0 | 0 | 17,626 | 0.064874 | none | 10 | 29,783 |
| 2 | completed | 2 / 0 | 0 | 19,298 | 0.020404 | none | 7 | 1,924 |
| 3 | completed | 1 / 0 | 0 | 19,951 | 0.006156 | none | 0 | 0 |
| 4 | completed | 2 / 1 | 0 | 20,160 | 0.101257 | none | 2 | 13,247 |
| 5 | completed | 1 / 0 | 0 | 11,248 | 0.003716 | none | 0 | 0 |
| 6 | completed | 3 / 0 | 0 | 12,370 | 0.011897 | none | 3 | 1,590 |
| 7 | completed | 1 / 0 | 0 | 12,560 | 0.003693 | none | 0 | 0 |
| 8 | completed | 1 / 0 | 0 | 12,778 | 0.003871 | none | 0 | 0 |

## confirm1.s17-docthread-confirm-6-guarded_clm.r1: per turn

| turn | ending | attempts main / summary | retries | peak reported input (tokens) | cost (USD) | notices | tool calls | tool chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | completed | 6 / 0 | 0 | 21,375 | 0.169687 | none | 11 | 35,808 |
| 2 | completed | 3 / 0 | 0 | 22,965 | 0.124178 | pressure 1 | 7 | 1,924 |
| 3 | completed | 2 / 0 | 0 | 5,882 | 0.019321 | none | 1 | 759 |
| 4 | completed | 11 / 0 | 0 | 26,583 | 0.383824 | pressure 2 | 17 | 107,394 |
| 5 | completed | 1 / 0 | 0 | 8,368 | 0.016573 | none | 0 | 0 |
| 6 | completed | 3 / 0 | 0 | 9,550 | 0.055952 | none | 3 | 1,590 |
| 7 | completed | 1 / 0 | 0 | 9,931 | 0.019851 | none | 0 | 0 |
| 8 | completed | 1 / 0 | 0 | 10,171 | 0.021051 | none | 0 | 0 |

## confirm1.s18-docthread-confirm-6-paper_clm_shell.r1: per turn

| turn | ending | attempts main / summary | retries | peak reported input (tokens) | cost (USD) | notices | tool calls | tool chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | completed | 7 / 0 | 0 | 21,578 | 0.083266 | none | 11 | 35,808 |
| 2 | completed | 2 / 0 | 0 | 23,251 | 0.018399 | none | 7 | 1,924 |
| 3 | completed | 1 / 0 | 0 | 23,551 | 0.006054 | none | 0 | 0 |
| 4 | context_limit | 12 / 0 | 0 | 30,089 | 0.153056 | over_limit 1, reminder 1, rollback 6, rollback_feedback 1 | 3 | 19,853 |
