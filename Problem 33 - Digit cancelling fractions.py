def part_num(number):
    x=str(number)
    t=[]
    s=len(x)
    for i in range(s):
        t.append(int(x[i]))

    return t

y=[]
z=[]

for i in range(10,100):
    for j in range(i+1,100):
        if i!=j and j<=99:
            a=part_num(i)
            b=part_num(j)
            if a[0] in b and a[1]!=b[1]:
                b.remove(a[0])
                a.remove(a[0])
                if a[0] not in b and b[0]!=0 and a[0]!=0 and a[0]/b[0] == i/j:
                    y.append([i,j])
                    z.append([a[0],b[0]])
            elif a[1] in b and a[1]!=b[1]:
                b.remove(a[1])
                a.remove(a[1])
                if a[0] not in b and b[0]!=0 and a[0]!=0 and a[0]/b[0] == i/j:
                    y.append([i,j])
                    z.append([a[0],b[0]])

print(y)
print(z)

q=1
for i in range(len(z)):
    q=q*z[i][0]
w=1
for i in range(len(z)):
    w=w*z[i][1]

print(q,w)
print(int(w/q))