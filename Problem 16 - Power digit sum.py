n=2**1000
n=str(n)
y=[]
t=0

for i in range(len(n)):
    y.append(int(n[i]))

for i in range(len(n)):
    t+=y[i]

print(t)