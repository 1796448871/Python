# 牛逼万能的eval函数
list1 = eval(input())
list=sorted(list1)
len=len(list)
print(f"元素个数：{len}")
print(f"最大值：{list[len-1]}")
print(f"最小值：{list[0]}")
# 获取总和
sum=0
for i in list:
    sum+=i
print(f"元素和：{sum}")
print(f"平均值：{sum/len}",end="")

# 在python3中print是一个函数，对于函数，其形参中有默认参数和关键参数。
# 我们发现，在结尾处出现了end = ‘\n’，说明print是以\n结束的，end是默认参数。
# 只要我们在print中将默认参数的值改为空或者空格，就能实现不换行。
