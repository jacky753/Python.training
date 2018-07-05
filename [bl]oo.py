import re 

sentens = "The ghost that says boo haunts the loo"
found = re.findall("[bl]oo", sentens, re.IGNORECASE)
print(found)
