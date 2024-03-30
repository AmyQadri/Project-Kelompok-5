class Car:
    def __int__ (self,name,brand,capacity):
        self.name = name
        self.brand = brand
        self.capacity = capacity
        self.position = (0,0)
        self.status_engine = False
    

    def cekcarinfo(self):
        print(f"Name Car : {self.name} \nCar brand : {self.brand} \nCar capacity : {self.capacity} \nCar position : {self.position} \nCar status_engine {self.status_engine}")

carme = Car("inova","toyota",40)
carme.cekcarinfo()







