x=[]
for i in range(20):
    x.append(i+1)
#print(x)
for i in range(20):
    for j in range(i,19):
        if x[j+1]%x[i]==0:
            x[j+1]=x[j+1]/x[i]
#print(x)
s=1
for i in range(20):
    s=s*x[i]
print(int(s))