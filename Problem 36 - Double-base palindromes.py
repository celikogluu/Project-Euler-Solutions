def isPalindrome(number):
    return str(number) == str(number)[::-1]

def dual_base(number):
    a=''
    b=number

    while b!=0:
        if b%2==0:
            a='0'+a
            b=int(b/2)
        else :
            a='1'+a
            b=int(b/2)

    return int(a)

x=[]

for i in range(1,10**6):
    if isPalindrome(i) and isPalindrome(dual_base(i)):
        x.append(i)

print(x)
print(sum(x))