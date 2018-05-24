def parts_of_number(number):
    a=str(number)
    b=[]
    for i in range(len(a)):
        b.append(int(a[i]))

    return b

def power_sum_parts_of_number(number):
    a = 0
    for i in range(len(parts_of_number(number))):
        a += parts_of_number(number)[i]**5

    return a

numbers = []
for i in range(2,1000000):
    if i == power_sum_parts_of_number(i):
        numbers.append(i)

print(sum(numbers))