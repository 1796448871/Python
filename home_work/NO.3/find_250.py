# 读取输入的整数列表,用map都转化成int类型给list
numbers = list(map(int, input().split()))

# 初始化计数器和最后一次出现“250”的位置
count = 0
last_250_index = 0

# 遍历整数列表
for i, num in enumerate(numbers):
    count += 1
    if num == 250:
        last_250_index = count

# 输出结果
print(last_250_index)