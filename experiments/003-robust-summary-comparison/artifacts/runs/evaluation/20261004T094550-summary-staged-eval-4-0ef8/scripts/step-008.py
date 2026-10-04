b='/task/fixtures/stage-3/logs/payments-api.log'
n=[i for i,l in enumerate(open(b),1) if 'db pool exhausted: 18/18' in l]
print(len(n),n[:5],n[-3:])