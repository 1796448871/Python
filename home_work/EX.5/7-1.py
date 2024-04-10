def switch_case(argument):
    switcher = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    # 如果参数不在字典中，则返回 "Invalid month"
    return switcher.get(argument, "Invalid month")

# 有一个问题,负数需要先转化成正数在进行操作
T=int(input())
is_fushu=False
for _ in range(T):
    str=''
    n, k = map(int, input().split())
    temp=n
    if(n<0):
        is_fushu=True
        n=abs(n)
    while(True):
        if(n==0):
            str='0'
            break
        yu=n%k
        str+=switch_case(yu)
        # 可以使用  //  运算符来进行整数相除
        shang=n//k
        n=shang
        if(shang==0):
            break
        #  简洁;负数推断之后再改回False
    if(is_fushu):
        print(temp,"-"+str[::-1])
        is_fushu=not is_fushu
    else:
        print(temp,str[::-1])
    


        
