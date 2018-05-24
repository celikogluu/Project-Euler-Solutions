collatz_length = [0] * 10**6
collatz_length[1] = 1
max_length = [1, 1]

for i in range(1, 1000000):
    n, s = i, 0
    x = []
    while n > 10**6 - 1 or collatz_length[n] < 1:
        x.append(n)
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3 * n + 1
        s += 1

    for j in range(s):
        m = x[j]
        if m < 10**6:
            new_length = collatz_length[n] + s - j
            collatz_length[m] = new_length
            if new_length > max_length[1]: max_length = [i, new_length]


print("%s at length %s" % (max_length[0], max_length[1]))