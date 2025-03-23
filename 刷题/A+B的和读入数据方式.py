import sys

try:
    while True:  #python只认识True,不认识true
        # 读取第一行，获取N
        N = int(input().strip())
        for _ in range(N):
            line = input().strip()#strip去前后空格
            a, b = map(int, line.split())  #split分割
            print(a + b)  # 输出a和b的和
except EOFError:
    pass  # 当没有更多输入时，捕获EOFError并结束程序


# 在try里面只能break  return 语句不能在全局作用域中使用