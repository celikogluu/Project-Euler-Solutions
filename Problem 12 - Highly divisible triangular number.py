def divisors(number):
    x=[]
    for i in range(1,number+1):
        if number % i == 0:
            if i < number/i :
                x.append(i)
                x.append(number/i)
            elif i == number/i :
                x.append(i)
            else :
                break
    
    return len(x)



sum_=1
step=1

while  divisors(sum_) <= 500 :
    step = step + 1
    sum_ += step

print(sum_)
    
