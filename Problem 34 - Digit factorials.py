def part_num(number):
    x=str(number)
    t=[]
    s=len(x)
    for i in range(s):
        t.append(int(x[i]))

    return t

def fact(number):
    x=1
    for i in range(number):
        x=x*(i+1)

    return x

numbers=[]
for i in range(10,2000001):
    q=part_num(i)
    a=0
    for j in range(len(q)):
       a=a+fact(q[j])
    if a==i :
        numbers.append(i)

print(numbers)
print(sum(numbers))