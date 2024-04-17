class Vecter3:
    def __init__(self,x = 0,y = 0,z = 0):
        self.X=x
        self.Y=y
        self.Z=z
    #当你调用类的方法时，不需要显式地传递     
    #self  参数，Python 会自动将对象实例传递给  self
    def add(self, n):
        r = Vecter3()
        r.X=self.X+n.X
        r.Y=self.Y+n.Y
        r.Z=self.Z+n.Z
        return r
    def __add__(self,n):
        r=Vecter3()
        r.X=self.X+n.X
        r.Y=self.Y+n.Y
        r.Z=self.Z+n.Z
        return r
    def __sub__(self,n):
        r=Vecter3()
        r.X=self.X-n.X
        r.Y=self.Y-n.Y
        r.Z=self.Z-n.Z
        return r
    def __mul__(self,n):
        r=Vecter3(0)
        r.X = self.X * n
        r.Y = self.Y * n
        r.Z = self.Z * n
        return r
    def __truediv__(self,n):
        r=Vecter3()
        r.X=self.X/n
        r.Y=self.Y/n
        r.Z=self.Z/n
        return r
    def __floordiv__(self,n):
        r=Vecter3(0,0,0)
        r.X=self.X//n
        r.Y=self.Y//n
        r.Z=self.Z//n
        return r
    def show(self):
        print((self.X,self.Y,self.Z))
def main():
    v1 = Vecter3(1,2,3)
    v2 = Vecter3(3,4,5)
    v3 = v1 + v2
    v3.show()
    v3 = v1.add(v2)
    v3.show()
    v4 = v1 - v2
    v4.show()
    v5 = v1 * 3
    v5.show()
    v6 = v2/2
    v6.show()
    v7 = v2//2
    v7.show()


main()
