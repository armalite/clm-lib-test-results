import sys; sys.path.insert(0, "/task/fixtures")
from handbook_tools import search, show
import subprocess
print(subprocess.run('grep -n -i "team-lead\\|team lead" /task/fixtures/handbook/*.md | cut -c1-250',shell=True,capture_output=True,text=True).stdout)
print(subprocess.run('grep -n -i "relocat" /task/fixtures/handbook/*.md | cut -c1-300',shell=True,capture_output=True,text=True).stdout)