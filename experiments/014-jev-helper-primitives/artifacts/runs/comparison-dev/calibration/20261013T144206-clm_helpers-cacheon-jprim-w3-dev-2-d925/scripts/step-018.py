import sys
sys.path.insert(0,'/task/workspace')
import regtool
c=regtool.load()
regtool.set_entry(c,'note1','Stages 1-6 implemented in core.py (eu filter removed, tests pass). Helper regtool.py (load,save,set_entry,affected). Next: advance to stage 7.','note')
c['entries']=[e for e in c['entries'] if e['id'] in('register','note1')]
regtool.save(c)
print('ok')