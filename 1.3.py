class Shape():
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.len = length
        self.wid = width
    
    def area(self):
        if self.len and self.wid is not None:
            return self.len*self.wid
        else:
            return super.area()
        
sq = Rectangle(3,4)
print(sq.area())

