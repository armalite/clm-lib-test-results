d='/task/fixtures/handbook/'
for n in [32,22,27,33,18,26,37,25,29,39]:
    t=open(d+'HB-%02d.md'%n).read().split('\n')
    print('==',n)
    for l in t[1:]:
        if l.strip(): print(l[:230])