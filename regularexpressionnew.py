import re
s="http://dimik.pub/book/30/programming-career-guideline-by-tamim-shahriar"
regex=re.compile(r'book/(\d+)/(\w+)-(\w+)')

result=re.findall(regex,s)
print(result)
print(type(result))
li=list(result[0])
print(li)
dir_result="-".join(li)
print(dir_result)