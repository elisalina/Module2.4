numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    if i > 1:
        flag = True
        for c in range(2, int(i / 2) + 1):
            if (i % c) == 0:
                flag = False
            break
        if flag:
            primes.append(i)
        else:
            not_primes.append(i)

print(not_primes)
print(primes)

