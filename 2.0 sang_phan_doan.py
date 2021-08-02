from math import *

prime = []


def sang_nguyen_thuy(delta):
    check = [True] * (delta + 1)
    for i in range(2, delta + 1):
        if check[i]:
            for j in range(2 * i, delta + 1, i):
                check[j] = False
            prime.append(i)
    for i in range(len(prime)):
        print(prime[i], end=' ')


def sang_phan_doan(n):
    delta = int(sqrt(n)) + 1
    sang_nguyen_thuy(delta)
    low = delta
    high = delta * 2
    while n > low:
        if high > n:
            high = n
        check = [True] * (delta + 1)
        for i in range(len(prime)):
            low_delta = int(low // prime[i]) * prime[i]

            if low_delta < low:
                low_delta += prime[i]
            for j in range(low_delta, high, prime[i]):
                check[j - low] = False
        for j in range(low, high):
            if check[j - low]:
                print(j, end=" ")
        low += delta
        high += delta

sang_phan_doan(100)

