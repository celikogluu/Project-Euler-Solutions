def factorial(number):
    r=1
    for i in range(number):
        r=r*(i+1)
    return r
k=0
while factorial(k)<10**6:
    print(k)
    k=k+1

a=''
c=''
b=[0,1,2,3,4,5,6,7,8,9]
x=10**6

while len(a)<11:
    x=x%factorial(k)
    k=k-1
    y=int(x/factorial(k))
    if x!=0 and x-y!=2:
        z=b[y]
        a=a+str(z)
        b.remove(z)
    elif x!=0 and x-y==2:
        a=a+str(b[1])
        b.remove(b[1])
    else :
        b.sort(reverse=True)
        for i in range(len(b)):
            a = a + str(b[i])

for i in range(len(a)-2):
    c=c+a[i]



print(c)
