def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m
        
        
x=int(input())
while True:
    try:
        for i in range(x):
        # 输入两个正整数
            m, n = input().split()
            m=int(m)
            n=int(n)
        # 调用函数计算最大公约数
            result = gcd(m, n)
            print( result)
    except EOFError:
        break