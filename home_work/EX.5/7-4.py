n=int(input())
# 装有list的List
studentList=[]
for _ in range(n):
    name,ds,db,c=input().split()
    ds=int(ds)
    db=int(db)
    c=int(c)
    studentList.append([name,ds,db,c])


newList=sorted(studentList,key=lambda s:s[1]+s[2]+s[3],reverse=True)
for i in range(len(newList) ):
    print(newList[i][0],newList[i][1],newList[i][2],newList[i][3],sep=' ')