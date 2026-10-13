import sys; sys.path.insert(0, "/task/fixtures")
from handbook_tools import search, show
r=search("annual training budget team lead", k=6)
print(r)