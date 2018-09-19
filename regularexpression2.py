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
match7=re.search('B.+h',d)
print(match7.group())
match8=re.search('B.+?h',d)
print(match8.group())
text="phone number: 01711101001 "
match9=re.search('\d+',text)
print(match9.group())
text1="House number :12 ,phone number: 01711101001 ."
match10=re.search('\d+',text1)
print(match10.group())
match11=re.search('\d{11}',text1)
print(match11.group())
print(match11)
text3="House number :12 ,phone number: 017 11101001 ."
match12=re.search('\d{3}\s*\d{8}',text3)
print(match12.group())
match13=re.search('\d{3}\s?\d{8}',text3)
print(match13.group())
text4="House number :12 ,phone number: 017 11101001,018 11101001,015 11101001,019 11101001,016 11101001 ."
match15=re.findall('\d{3}\s*\d{8}',text4)
print(match15)
