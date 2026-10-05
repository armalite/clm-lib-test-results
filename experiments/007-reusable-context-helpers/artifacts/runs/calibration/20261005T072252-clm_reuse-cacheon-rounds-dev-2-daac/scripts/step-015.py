from ctx import keep_notes
import json
n=json.load(open('context.json'))['entries'][0]['body']
keep_notes(n+'\nR5: board.md:3 Thread A mitigated (CHG-143 APPLIED inventory-svc changes.md:3); board.md:4 Thread B +shipping-svc; board.md:5 OPEN VENDOR_TICKET, :6 OPEN ALERT_TUNING. logs: auth-svc.log:11-64, shipping-svc.log:9-65 cert_expired sso; checkout/inventory/search 0 errs.')