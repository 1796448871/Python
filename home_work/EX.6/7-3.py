import math
import decimal
class Rect:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def are(self):
        return self.a * self.b

    def length(self):
        return (self.a + self.b) * 2


class Cubic(Rect):
    def __init__(self, a, b, c):
        super(Cubic, self).__init__(a, b, c)

    def are(self):
        t1 = (self.a * self.b + self.a * self.c + self.c * self.b) * 2
        # t1=0
        print("%.2f" %t1, end=' ')

    def v(self):
        v1 = super(Cubic, self).are() * self.c
        # v1=0
        print("%.2f" % v1, end=' ')


class Pyramid(Rect):
    def __init__(self, a, b, c):
        super(Pyramid, self).__init__(a, b, c)

    def are(self):
        t2 = self.a * self.b + self.b * math.sqrt(self.c ** 2 + (self.a / 2) ** 2) + math.sqrt(self.c ** 2 + (self.b / 2) ** 2) * self.a
        print("%.2f" % t2, end=' ')

    def v(self):
        v2 = super(Pyramid, self).are() * self.c / 3
        print("%.2f" % v2)


while True:
    try:
        a, b, c = map(float, input().split())
        if (a <= 0 or b <= 0 or c <= 0):
            print("0.00 0.00 0.00 0.00")
        else:
            cu = Cubic(a, b, c)
            cu.are()
            cu.v()

            p = Pyramid(a, b, c)
            p.are()
            p.v()
    except:
        break