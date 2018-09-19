import re

s="Bangladesh"
match1=re.search(".",s)
print(match1.group())
match2=re.search("B..g",s)
print(match2.group())
d="Bangladesh is our homeland"
match3=re.search("............",d)
print(match3.group())
match4=re.search("o\w\w",d)
print(match4.group())
# match5=re.search("i\w\w",d)
# print(match5.group())
match6=re.search('B\w+h',d)
print(match6.group())

