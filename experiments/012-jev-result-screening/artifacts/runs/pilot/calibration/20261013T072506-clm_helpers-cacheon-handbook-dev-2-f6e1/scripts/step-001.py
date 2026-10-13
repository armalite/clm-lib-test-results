import sys; sys.path.insert(0, '/task/fixtures')
from handbook_tools import search
for q in ['mileage rate petrol car','relocation lump sum another country','home-office equipment allowance','meal allowance intern client-site Paris','training budget team lead','purchase approval threshold facilities']:
    r=search(q,k=5)
    print(str(r)[:900])
