def fibonacci(number):
    x=[1,1]
    for i in range(2,number):
        x.append(x[i-1]+x[i-2])
    return max(x)
n=3
while len(str(fibonacci(n)))<1000:
    n=n+1

print(len(str(fibonacci(n))))
print(n)
