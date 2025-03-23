import sys

try:
    while True:  # 持续读取输入，直到没有更多输入
        # 读取第一行，获取N
        N = int(input().strip())
        
        # 读取接下来的N行，每行包含两个整数a和b
        for _ in range(N):
            line = input().strip()
            a, b = map(int, line.split())  # 将字符串分割并转换为整数
            print(a + b)  # 输出a和b的和
except EOFError:
    pass  # 当没有更多输入时，捕获EOFError并结束程序