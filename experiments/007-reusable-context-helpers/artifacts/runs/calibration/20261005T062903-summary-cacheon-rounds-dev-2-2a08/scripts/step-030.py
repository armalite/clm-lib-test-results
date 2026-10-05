import os,json
b='/task/fixtures/round-10/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(os.listdir(b+'logs')):
    d={}
    for i,l in enumerate(open(b+'logs/'+f)):
        try:j=json.loads(l)
        except: j={'level':'?','msg':l[:60]}
        if j.get('level') in('ERROR','?'):
            m=j.get('msg');c=d.get(m,(0,i+1,0));d[m]=(c[0]+1,c[1],i+1)
    print(f,d)
open('/task/workspace/notes.md','a').write('\nR10 read step30\n')