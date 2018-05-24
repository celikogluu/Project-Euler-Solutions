k = 0
x=[1]
for i in range(500):
   k += 2
   a = x[-1]
   for j in range(4):
       x.append(a + k*(j+1))

print(x)
print(sum(x))
