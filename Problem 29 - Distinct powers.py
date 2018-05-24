a = [i for i in range(2,101)]
b = a
x=[]

for i in a:
    for j in b :
        if i**j not in x :
            x.append(i**j)

print(len(x))