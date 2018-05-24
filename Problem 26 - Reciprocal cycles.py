def primes(number):
    x=[]
    y=[]
    for i in range(1,number):
        x.append(i+1)

    for i in range(len(x)-1):
        for j in range(2,x[i+1]):
            if x[i+1]%j==0:
                y.append(x[i+1])
                break
    for i in range(len(y)):
        x.remove(y[i])
    return x
q=1000
print('Primes :',primes(q))

p=primes(q)
z=[0,1,6]

for i in range(3,len(p)):
    for j in range(1,p[i]):
        if 10**j % p[i] ==1:
            z.append(j)
            break



print(p[z.index(max(z))])