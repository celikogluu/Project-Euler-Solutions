a=input('Enter a number:')
a=int(a)
d=[]
c=[]
import math

for i in range(int(math.sqrt(a))+1):
    if a%(i+1)==0:
        d.append(i+1)
        print(d)
print(d)
k=len(d)
for t in range(1,k):
    for i in range(len(d)-t-1):
        if d[i+t+1]%d[t]==0 :
            c.append(d[i+t+1])
            print(c)
for i in range(len(c)):
    if c[i] in d :
        d.remove(c[i])
    else:
        continue
print(max(d))