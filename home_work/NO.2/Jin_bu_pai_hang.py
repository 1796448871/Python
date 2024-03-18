# eval()可以自动转化input输入的字符串成:整数或浮点数等
t = eval(input())

for i in range(t):
    n = eval(input())
    s = {}
    for i in range(n):
        # 将这行输入按照空格分隔后分别赋值给变量  stu 、 kv  和  sco
        # 输入用户名，进步总数，解题总数
        stu, kv, sco = input().split()
        s[stu] = [eval(kv), eval(sco)]
    rank = 0
    val = 0
    kv_val = 0
    # enumerate()  是 Python 中的一个内置函数，用于同时遍历数据集的索引和值
    #                                                          按照进步  按照解题      按照用户名   升序
    #                                         x的存储类似这样:('usx15131',[21,124])
    for index, i in enumerate(sorted(s.items(), key=lambda x: (x[1][0], x[1][1], -int(x[0][3:])), reverse=True)):
        # 防止相同的逻辑
        if i[1][0] != val or kv_val != i[1][1]:
            rank = index + 1
        print(rank, i[0], i[1][0], i[1][1], sep=" ")
        val = i[1][0]
        kv_val = i[1][1]
