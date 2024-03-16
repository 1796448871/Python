n = int(input())
fib = [1, 1]  # 斐波拉契数列的前两项
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])  # 计算第i项并添加到[列表]
for i in range(n):
    if i % 5 == 0 and i!=0:
        print()  # 每行显示5个数，需要换行
    print("%6d" % fib[i], end='')  # 每个数占6列宽度
