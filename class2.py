class Car:
    def __init__ (self,name,brand,capacity):
        self.name = name
        self.brand = brand
        self.capacity = capacity
        self.speed = 0
        self.status_engine = False
    

    def CheckCarInfo(self):
        print(f"Name Car : {self.name} \nCar brand : {self.brand} \nCar capacity : {self.capacity} \nCar position : {self.position} \nCar status_engine {self.status_engine}")

    def StarEngine(self):
        self.status_engine = True
    def StopEngine(self):
        self.status_engine = False

    def Accelerate (self,speed):
        self.speed = speed
        if speed > 0:
            self.position = (self.position[0] + speed, self.position[1])
        else:
            self.position = (self.position[0], self.position[1] - speed)







