class Car:
    def __init__ (self,name,brand,capacity):
        self.name = name
        self.brand = brand
        self.capacity = capacity
        self.position = (0,0)
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

    def FuelConsumption(self):
        if self.speed > 100:
            self.capacity -= 10
        elif self.speed >= 60 <= 100:
            self.capacity -= 6
        elif self.speed >= 50 <= 60:
            self.capacity -= 5
        elif self.speed >= 40 <= 50:
            self.capacity -= 4
        elif self.speed >= 30 <= 40:
            self.capacity -= 3
        elif self.speed >= 20 <= 30:
            self.capacity -= 2
        else:
            self.capacity -= 1
        

     
        


