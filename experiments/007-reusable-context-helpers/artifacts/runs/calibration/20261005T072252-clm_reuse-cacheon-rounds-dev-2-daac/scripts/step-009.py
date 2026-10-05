from ctx import keep_notes
import json
n=json.load(open('context.json'))['entries'][0]['body']
keep_notes(n+' R3 logs: auth-svc.log:6-72 ERROR tls certificate_expired peer=sso.example.net (board says DB pool - likely wrong cause); checkout-api.log:33-74, inventory-svc.log:3-50 dns SERVFAIL; search-api 0 errs.')