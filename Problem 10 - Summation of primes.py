import math
def isPrime(number):
    if number % 2 == 0:
        return False
    for current in range(3, int(math.sqrt(number) + 1), 2):
        if number % current == 0:
            return False
    return True

sum=5
number=5

while number <= 2000000 :
    if number <= 2000000 and isPrime(number) == True :
        sum += number
    number += 2

print(sum)