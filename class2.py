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
        print("Engine has been started!")
    def StopEngine(self):
        self.status_engine = False
        print("Engine has been stopped!")

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

    def Refuel(self):
        print("Menu Bahan Bakar ::")
        print("1. 10 Liter (10.000) \n2. 20 Liter (20.000) \n3. Full Tank")
        MasukanBahanBakar = int(input("Masukan Bahan Bakar Yang Ingin Diisi :"))
        if MasukanBahanBakar == 1:
            self.capacity += 10
            print("Bahan Bakar Sudah Diisi!")
        elif MasukanBahanBakar == 2:
            self.capacity += 20
            print("Bahan Bakar Sudah Diisi!")
        elif MasukanBahanBakar == 3:
            self.capacity = 33
            print("Bahan Bakar Sudah Diisi!")
        else:
            print("Invalid Menu!")
