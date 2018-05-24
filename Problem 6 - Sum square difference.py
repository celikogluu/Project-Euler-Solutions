a=100
x=[]
for i in range(a):
    x.append(i+1)
#print(x)
z=0
for i in range(a):
   for j in range(i+1,a):
       z=z+x[i]*x[j]
print(2*z)