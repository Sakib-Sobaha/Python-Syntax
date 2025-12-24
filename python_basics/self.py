class Circle:
    def __init__(self, r):
        self.r = r 

    def circumference(self):
        return 2 * 3.14 * self.r
    
    def area(self):
        return 3.14 * self.r**2
    

c = Circle(7)
print("Circumference:", c.circumference())
print("Area:", c.area())