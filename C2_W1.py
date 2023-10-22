import re
count=0
sum=0
fh = open('test.txt')
for line in fh:
    stuff=re.findall('[0-9]+',line)
    if len(stuff) != 0:
        x=int(len(stuff))
        while x!=0:

            sum=sum+float(stuff[x-1])
            count=count+1
            x=x-1
print("Sum is : "+str(sum))
print("Count is : "+str(count))
