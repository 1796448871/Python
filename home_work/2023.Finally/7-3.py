N, *numbers = map(int, input().split())

# 建立一个字典
count_dict = {}
for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# 函数  max() ，它接受一个可迭代对象和一个关键字参数  key
max_num = max(count_dict, key=count_dict.get)
max_count = count_dict[max_num]

print(max_num, max_count)