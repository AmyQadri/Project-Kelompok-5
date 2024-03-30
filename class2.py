class Car:
    def __init__ (self,name,brand,capacity):
        self.name = name
        self.brand = brand
        self.capacity = capacity
        self.position = (0,0)
        self.status_engine = False
    

    def cekcarinfo(self):
        print(f"Name Car : {self.name} \nCar brand : {self.brand} \nCar capacity : {self.capacity} \nCar position : {self.position} \nCar status_engine {self.status_engine}")

<<<<<<< HEAD
    def star_engine(self):
        self.status_engine = True
    def stop_engine(self):
        self.status_engine = False







=======

carme = Car("Innova","Toyota",40)
carme.cekcarinfo()
>>>>>>> 16e1a23 (Buat Surya)
