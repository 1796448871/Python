# 假设n是一个正整数，它的值不超过1000000，请编写一个程序，将n分解为若干个素数的乘积。
def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(str(i))
    if n > 1:
        factors.append(str(n))
    return factors

T=int(input())
for _ in range(T):
    i=int(input())
    factors = prime_factors(i)
    print("*".join(factors))