
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