import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=" R4 logs: checkout-api.log:18-20 heap high rss WARN (MEMORY_LEAK? board says rate limit; check 429 later), lines 34-90 more; search-api.log:12,13,21,38,54,62 disk usage high /var/data (DISK_PRESSURE confirmed). R4 done -> advance next."
json.dump(c,open('/task/workspace/context.json','w'))