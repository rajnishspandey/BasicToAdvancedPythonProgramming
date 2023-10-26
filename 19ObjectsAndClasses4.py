class Vehicle:
    color = "white"
    #contructor
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    #method
    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)

# Creating objects of the Vehicle class
vehicle1 = Vehicle(200, 50000)
vehicle1.assign_seating_capacity(5)
vehicle1.display_properties()

vehicle2 = Vehicle(180, 75000)
vehicle2.assign_seating_capacity(4)
vehicle2.display_properties()
