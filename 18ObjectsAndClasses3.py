class Rectangle(object):
    #constructor
    def __init__(self,width =2, height =3, color = 'red'):
        self.width = width
        self.height = height
        self.color = color
    
rectangle = Rectangle()
print(f"{rectangle.height} and {rectangle.width} for the colour of {rectangle.color} rectangle")
