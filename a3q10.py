def Armstrong(n):
    d = 0
    while n != 0:

        m = int(n % 10)
        d = int((m ** 3) + d)
        n = n // 10

    return d


for i in range(100, 1000):
    k = int(Armstrong(i))
print(k, " ")
