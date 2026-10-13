import json,re
d='/task/fixtures/round-07/logs/pricing-svc.log'
h=[(i,l) for i,l in enumerate(open(d),1) if re.search(r'mem|heap|restart|rss',l,re.I)]
print(len(h),h[0][0] if h else '',h[-1][0] if h else '',h[0][1][:200] if h else '')
c=json.load(open('/task/workspace/context.json'))
b=c['entries'][0]['body']+"\nR7: board.md:3 Thread B revised DNS_RESOLUTION (inventory-svc). board.md:4 Thread D MEMORY_LEAK pricing-svc ongoing. CHG-153 PROPOSED irrelevant. inventory-svc.log:1-65 DNS SERVFAIL continues. Mem lines pricing: %d %s-%s"%(len(h),h[0][0] if h else '',h[-1][0] if h else '')
c={'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':b}]}
json.dump(c,open('/task/workspace/context.json','w'))