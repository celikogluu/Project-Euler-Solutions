def prime(number):
    for i in range(3,int(number**0.5)+1,2):
        if number % i == 0:
            return False

    return True

def part_num(number):
    x=str(number)
    t=[]
    s=len(x)
    for i in range(s):
        t.append(int(x[i]))

    return t

def comb(list):
    a=''
    for i in range(len(list)):
        a=a+str(list[i])

    return int(a)

def cycle(list):
    y=[]
    for i in range(len(list)):
        q=(i+1)%len(list)
        y.append(list[q])

    return y

primes=[2]
cycle_primes=[]
for i in range(3,10**6,2):
    if prime(i) :
        primes.append(i)
print(primes)

for i in range(len(primes)):
    t=part_num(primes[i])
    k=part_num(primes[i])
    f=[]
    for j in range(len(t)):
        k=cycle(k)
        p=comb(k)
        if p in primes:
            f.append(p)
    if len(f)==len(t) and f[0] not in cycle_primes:
        cycle_primes+=f

print(cycle_primes)
print(len(cycle_primes)-1)


