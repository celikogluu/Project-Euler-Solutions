from math import ceil

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        else:
            for i in range(3,int(ceil(number**0.5))+1,2):
                if number % 2 == 0:
                    return False
                elif number % i == 0 and number != i:
                    return False
    else :
        return False

    return True

def quadratic_prime(x,y,z):
    f = z**2 + x*z + y
    return f

b = []

for i in range(1000):
    if is_prime(i) == True:
        b.append(i)
        b.append(-i)

b.sort()

a = b

p = []

for i in range(-1000,1001) :
    for j in range(-999,1000) :
        k = 0
        for n in range(abs(i)):
            if is_prime(quadratic_prime(j,i,n)) == True:
                k += 1
            else :
                break
        p.append([k,i*j])
        m=max(p[:])
        print(m)
        p=[m]
