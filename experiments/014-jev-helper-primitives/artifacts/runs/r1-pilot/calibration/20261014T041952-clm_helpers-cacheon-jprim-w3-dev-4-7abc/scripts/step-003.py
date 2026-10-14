import sys;sys.path.insert(0,'/task/workspace')
import regmaint
c=regmaint.load();c['entries']=[e for e in c['entries'] if not e['id'].startswith('s2.')];regmaint.save(c);print(len(c['entries']))