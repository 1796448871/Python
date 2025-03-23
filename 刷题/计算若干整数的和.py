try:
    while True:  #python只认识True,不认识true
        line = input().strip().strip()#strip去前后空格
        my_list = list(map(int, line.split()))  #split分割
        num=my_list[0]
        if num==0:
            break
        sum1=0
        for i in range(1,num+1):
            sum1+=my_list[i]
        print(sum1)  # 输出a和b的和
except EOFError:
    pass  # 当没有更多输入时，捕获EOFError并结束程序


# 在try里面只能break  return 语句不能在全局作用域中使用