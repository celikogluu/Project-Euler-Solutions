def d(s):
    x=[]
    for i in range(1,s):
        if s%i==0:
            x.append(i)
    return x
y=[]

for n in range(1,10001):
    t=sum(d(n))
    if sum(d(t))==n and n!=t:
        y.append(n)
        print(y)

print(sum(y))