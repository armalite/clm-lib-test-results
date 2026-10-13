import sys,json;sys.path.insert(0,'/task/workspace')
import cm
n=json.load(open('/task/workspace/context.json'))['entries'][0]['body']
n=n.replace(' Next: advance to R9.','')
cm.setnotes(n+' R9: round-09/board.md:3 Thread C note pods restarting, investigating. search-api config err round-09/logs/search-api.log:2-33; disk shipping round-09/logs/shipping-svc.log:8-13 notify round-09/logs/notify-worker.log:4-8. No DNS. Next: advance to R10.')
print('ok')