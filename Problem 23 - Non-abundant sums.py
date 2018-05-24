def divisors(number):
    divisors_=[1]
    for i in range(2,number) :
        if number%i == 0 :
            if i < number/i :
                divisors_.append(i)
                divisors_.append(number/i)
            elif i == number/i :
                divisors_.append(i)
            else :
                break
    return sum(divisors_)

abundant_numbers=[]

for i in range(12,28124):
    if i < divisors(i):
        abundant_numbers.append(i)

print(abundant_numbers)

sum_two_abundant_number=[]

for i in range(len(abundant_numbers)):
    for j in range(i,len(abundant_numbers)):
        if abundant_numbers[i]+abundant_numbers[j]<28124 and abundant_numbers[i]+abundant_numbers[j] not in sum_two_abundant_number:
            sum_two_abundant_number.append(abundant_numbers[i]+abundant_numbers[j])


sum_=(28123*28124)/2

x=sum(sum_two_abundant_number)

print(int(sum_ - x))



sum_=(28123*28124)/2

x=sum(sum_two_abundant_number)

print(int(sum_ - x))
