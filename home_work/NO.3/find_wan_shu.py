def factors_sum(num):
    factors = [1]
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            # 直接存入两个数，除数和被除数
            factors.extend([i, num//i])
    # set()主要作用是去重
    return sum(set(factors))

def find_perfect_numbers(m, n):
    perfect_numbers = []
    for num in range(m, n+1):
        if factors_sum(num) == num:
            perfect_numbers.append(num)
    return perfect_numbers

m = int(input("请输入正整数 m："))
n = int(input("请输入正整数 n："))

if m > n:
    m, n = n, m

result = find_perfect_numbers(m, n)
if result:
    print(f"{m} 和 {n} 之间的完数有：{result}")
else:
    print(f"{m} 和 {n} 之间没有完数。")




    """ import math

# 判断一个数是否为完数
def is_perfect_number(num):
    factors = [1]  # 初始化因子列表，包含1
    sqrt_num = int(math.sqrt(num))
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)
    return sum(factors) == num

# 读取输入的两个正整数m和n
m, n = map(int, input().split())

perfect_numbers = []

for num in range(m, n + 1):
    if is_perfect_number(num):
        perfect_numbers.append(num)

if len(perfect_numbers) == 0:
    print("None")
else:
    for num in perfect_numbers:
        factors = [1]  # 初始化因子列表，包含1
        sqrt_num = int(math.sqrt(num))
        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                factors.append(i)
                factors.append(num // i)
        factors.sort()  # 将因子列表排序
        factors_str = ' + '.join(str(factor) for factor in factors)  # 构造因子累加形式的分解式
        print("{} = {}".format(num, factors_str)) """