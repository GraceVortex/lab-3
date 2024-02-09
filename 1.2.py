class Shape():
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, len):
        self.length = len
    
    def area(self):
        if self.length is not None:
            return self.length ** 2
        else:
            return super().area()

sq = Square(4)
print(sq.area())

    