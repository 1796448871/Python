class sentence(object):
    def __init__(self,name):
        self.name=name
    def printIt(self):
        print("输入的字符串是：",self.name,end="，")
    def printCount(self):
        print("共有",end="")
        print(len(self.name),end="")
        print("个字符")
    def intoList(self):
        print("其中有单词：",(self.name).split(),"，共有",end="")
        print(len(self.name.split()),end="")
        print("个单词。")
 
inp=str(input())
d=sentence(inp)
d.printIt()
d.printCount()
d.intoList()
inp2=inp.upper()
e=sentence(inp2)
e.printIt()
e.printCount()
e.intoList()