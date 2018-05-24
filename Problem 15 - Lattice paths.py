#The number of lattice paths in the nxn type is (2n)! / (n! * n!).

n=20
s=2*n
k=1
l=1
for i in range(s):
   k=k*(i+1)

for i in range(n):
    l=l*(i+1)


print(int(k/l/l))

