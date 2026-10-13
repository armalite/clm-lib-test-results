import json
p='/task/workspace/context.json'
c=json.load(open(p))
keep=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
keep.append({'id':'n4','role':'note','body':'R4: round-04/board.md:3 Thread B inventory-svc suspected CERT_EXPIRED ongoing; but logs show DNS SERVFAIL host=kms.internal round-04/logs/inventory-svc.log:16-34 (likely DNS_RESOLUTION, watch board). :4 OPEN CAPACITY_REVIEW. CHG-131 APPLIED TLS ticket rotation (changes.md:3). Thread A 429s continue pricing-svc.log:11-27, search-api.log:10-14. checkout/shipping clean. Next: advance to R5.'})
c['entries']=keep
json.dump(c,open(p,'w'))