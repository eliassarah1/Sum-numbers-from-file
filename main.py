import re

with open('tt.txt','r') as f:
    numlist = []
    for i in f:
        rslt = re.findall('[0-9]+',i)
        if len(rslt) > 0:
            for i in rslt:
                numlist.append(i)
print(numlist)
print(len(numlist))
x = 0
for i in numlist:
    x += int(i)
print(x)
