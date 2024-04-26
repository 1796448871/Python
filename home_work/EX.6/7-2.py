class sentence(object):
    def __init__(self,name):
        self.name=name
    def getSectence(self):
        return "输入的字符串是："+ self.name
    def getLength(self):
        return "，"+"共有"+str(len(self.name))+"个字符。"
    def getNumWords(self):
        return"其中有单词："+str((self.name).split())+"，共有"+str(len(self.name.split()))+"个单词。"
    def getWords(self):
        return str(self.name.split())
    def setSentenceUp(self):
        self.name=str.upper(self.name) 
        return self
    def __str__(self):
        return self.getSectence()+self.getLength()+"\n"+self.getNumWords()
 
inp=sentence(str(input())) 
print(inp)
inp2=inp.setSentenceUp()
print(inp2)
