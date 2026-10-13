import subprocess,json
print(open('/task/fixtures/round-01/changes.md').read())
print(subprocess.run('grep -nvE "slow query| INFO " -r /task/fixtures/round-01/logs | head -20',shell=True,capture_output=True,text=True).stdout[:2500])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; logs mostly INFO + benign slow query WARNs (230-440ms) in all 5 services (notify-worker,checkout-api,auth-svc,payments-svc,search-api).'}]}
json.dump(c,open('/task/workspace/context.json','w'))