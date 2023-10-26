#calling objects using dot(.) method object.method()
class Car:
    #class attributed shared by all then instances of the class
    max_speed  = 120 

    #constructor method
    def __init__(self,make,model,color,speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed #intial speed  = 0

    #method for accelerating the car
    def accelerate(self,acceleration):
        if self.speed+acceleration <= Car.max_speed:
            self.speed += acceleration
        else:
            self.speed = Car.max_speed

    #methof to get the current speed of the car
    def get_speed(self):
        car1 = Car("Toyota", "Camry", "Blue")
        car2 = Car("Honda", "Civic", "Red")

        #accelerate the cars
        car1.accelerate(30)
        car2.accelerate(20)

        # Print the current speeds of the cars
        print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")
        print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h.")