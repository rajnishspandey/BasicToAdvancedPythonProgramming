class Circle(object):
    
    def __init__(self,radius = 3, colour ='Green'):
        self.radius = radius
        self.colour = colour

    #method
    def add_radius(self,r):
        self.radius = self.radius + r
        return (self.radius)
    
RedCircle = Circle(10,"Red")
print(f"radius is {RedCircle.radius} and colour of the circle is {RedCircle.colour}")

