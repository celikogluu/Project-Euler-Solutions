k=1
for i in range(100):
    k=k*(i+1)
#print(k)
s=str(k)

t=0
for i in range(len(s)):
   t=t+int(s[i])
print(t)
