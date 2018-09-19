import re
match=re.search('bangla','bangladesh')

print(match)
print(match.group())

match1=re.search('desh','bangladesh')
print(match1)
print(match1.group())

match2=re.search('des','bangladesh')
print(match2)
print(match2.group())

match3=re.search('det','bangladesh')
print(match3)
print(match3.group())
print(type(match))

# match is None

