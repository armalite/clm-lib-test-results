for i,l in enumerate(open('/task/fixtures/round-07/logs/search-api.log'),1):
  if 'ERROR' in l: print(i,l[60:200])
import os;print(os.listdir('/task/fixtures/round-07'))