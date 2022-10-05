import re

with open("week04/names.txt") as f:
  print()
  fin = f.read()
  print(fin)
  print()
  print(re.findall(r"\bChanna", fin))
  print(re.findall(r"\bDr.", fin))
  print(re.findall(r"\bVanitha", fin))
  print(re.findall(r"\bKumar", fin))
  print(re.findall(r"\bDadkar", fin))
  print(re.findall("S", fin))
  print(re.findall(r"\bShaydon", fin))
  print(re.findall(r"\bBodemar", fin))
  print(re.findall(r"\bSamynathan", fin))