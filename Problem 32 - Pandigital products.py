numbers = [i for i in range(1,10)]
def list_(a,b,c):
    x=[]
    for i in range(len(str(a))):
        x.append(int(str(a)[i]))

    for i in range(len(str(b))):
        x.append(int(str(b)[i]))

    for i in range(len(str(c))):
        x.append(int(str(c)[i]))

    x.sort()
    return x

y=[]
t=[]
z=str(int((987654321)**0.5))
w=[]
for i in range(len(z)):
    w.append(int(z[i]))

w.sort()
z=''
for i in range(len(w)):
    z += str(w[i])

limit=int(z)+1

for i in range(1,9999):
    for j in range(i,9999):
        if list_(i,j,i*j) == numbers and i*j not in y:
            y.append(i*j)
            t.append([i*j,i,j])
            print(t)

print(sum(y))
