import math
class Shape:
    def __init__(self,sName):
        self.sName=sName
             
class Rectangle(Shape):
    def __init__(self,sName,height,wight):
        super().__init__(sName)
        self.height=height
        self.wight=wight
    def getArea(self):
        return self.height*self.wight
    
class Circle(Shape):
    def __init__(self,sName,redius):
        super().__init__(sName)
        self.redius=redius
    def getArea(self):
        return math.pi*self.redius**2


