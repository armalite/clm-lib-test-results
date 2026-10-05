from ctx import keep_notes
import json
n=json.load(open('context.json'))['entries'][0]['body']
keep_notes(n+'\nR6: board.md:3 OPEN RUNBOOK_UPDATE. changes CHG-144 log sampling (irrelevant). auth-svc.log:4-79, shipping-svc.log:1-64 cert_expired sso; others 0 errs.')