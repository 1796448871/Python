T=int(input())
for i in range(T):
    n=int(input())
    all=[]
    for num in range(n):
        s,d=input().split() # 带空格时，自动拆分你的输入
        all.append((s,int(d))) # 将s，d打包为“元组”
    all.sort(key=lambda x: (-x[1]))
    # lambda接受一个参数 x，然后返回了一个值 -x[1]，表示取 x 中索引为 1 的元素，并返回其相反数。 
    for k in range(len(all)):
        print(k+1, all[k][0], all[k][1]) #输出排名、队名和解题数量

