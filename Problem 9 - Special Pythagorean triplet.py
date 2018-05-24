x=[i+1 for i in range(1000)]
for i in range(len(x)):
    for j in range(len(x)):
        k=1000-x[i]-x[j]
        if (x[i]**2)+(x[j]**2)==k**2 :
            print(x[i],x[j],k)
            print(x[i]*x[j]*k)
            break

