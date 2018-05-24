a1,a2,a3,a4,a5,a6,a7,a8 = 1,2,5,10,20,50,100,200

a=0
for i8 in range(2) :
    for i7 in range(3):
        for i6 in range(5):
            for i5 in range(11):
                for i4 in range(21):
                    for i3 in range(41):
                        for i2 in range(101):
                            for i1 in range(201):
                                if i1*a1+i2*a2+i3*a3+i4*a4+i5*a5+i6*a6+i7*a7+i8*a8 == 200:
                                    a += 1
                                elif i1*a1+i2*a2+i3*a3+i4*a4+i5*a5+i6*a6+i7*a7+i8*a8 > 200:
                                    break

print(a)