while True:
    try:
        all=[]
        n=int(input())
        # extend类似append，但是它可以添加一个序列
        all.extend(range(1,n+1))
        # 计数用，记录当前的下标
        jishu=0
        while(len(all)!=1):
            #此逻辑通用：如果+1之后大于len就重置到最初的位置 
            if((jishu+1)>(len(all)-1)):
                jishu=0
            #如果没有大于len，就+1 
            else:
                jishu+=1


            if((jishu+1)>(len(all)-1)):
                jishu=0
            else:
                jishu+=1

            #删除被锁定的序列位置 
            del all[jishu]
            #因为len-1了，所以jishu位置也要-1
            jishu-=1

            
            if((jishu+1)>(len(all)-1)):
                jishu=0
            else:
                jishu+=1
        #最后只剩下一个了，就是我们需要的
        print(all[0])
    except EOFError:
        break

    # 经验:try except是为了解决多次输入数组。
    