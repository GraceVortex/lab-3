import math
class Point():
    def __init__(self,x,y,x1,y1):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1

    def show(self):
        return self.x, self.y, self.x1, self.y1
    
    def move(self):
        return self.x+2 ,self.y+2, self.x1+2 ,self.y1+2,
    
    def distance(self):
        dist = (self.x  - self.x1)**2 + (self.y - self.y1)**2
        distrt =  math.sqrt(dist)
        return distrt
    
sq = Point(1,2,3,4)
print(sq.show())
print(sq.move())
print(sq.distance())