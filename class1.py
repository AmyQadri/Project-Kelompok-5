class User:
    AmountOfWork = 0
    def __init__ (self, name, age,cash, email):
        self.name = name
        self.age = age
        self.energy = 100
        self.cash = cash
        self.email = email
        self.notelocation = ()
        self.user_level = 0
        self.reward_point = 0


    def UserInfo(self):
        print(f"Name : {self.name} \nAge : {self.age} \nEnergy : {self.energy} \nCash : {self.cash} \nEmail : {self.email} \nUser_level : {self.user_level} \nReward_point : {self.reward_point} \nnoteLocation : {self.notelocation} m")


    def Working(self,Driver,CarMe):
        if CarMe.status_engine == True:
            print("Tentukan Titik Penjemputan")
            Driver.PickUp()
            print("Tentukan Titik Tujuan")
            Driver.DropOff()
            print("Jarak Yang Akan Ditempuh Adalah :",Driver.Distance())
            if self.energy > 0:
                if Driver.distance >= 100 :
                    Driver.cosh = 10000
                    self.cash += 10000 - 1000
                    self.reward_point += 10
                elif Driver.distance >= 50 :
                    Driver.cosh = 5000
                    self.cash += 5000 - 1000
                    self.reward_point += 5
                elif Driver.distance >= 20 :
                    Driver.cosh = 3000
                    self.cash += 3000 - 1000
                    self.reward_point += 3
                elif Driver.distance >= 10 :
                    Driver.cosh = 2000
                    self.cash += 2000 - 1000
                    self.reward_point += 2
                else :
                    Driver.cosh = 1000
                self.energy -= 3
                
                self.AmountOfWork += 1
                if self.AmountOfWork >= 2 :
                    self.user_level  += 1
                else:
                    pass
                
            else:
                print("Energy Tidak Cukup")
            print("Biaya Yang Harus Dibayarkan : ",Driver.cosh)
        else:
            print("Mesin Kendaraan Belum Hidup!")

    def RunCarForWorking(self,car):
        if car.status_engine == True :
            if car.capacity  > 0 :
                speed = int(input("Masukan Speed :"))
                print("Mobil Dijalankan Dengan Kecepatan : ",speed)
                car.Accelerate(speed)
                if speed >= 10 <= 20 :
                    self.notelocation  += 1000,2000
                elif speed >= 20 <= 50 :
                    self.notelocation.random += 2000,3000
                elif speed >= 50 <= 100 :
                    self.notelocation.random += 3000,4000
                else:
                    print("Lokasi Terlalu Jauh, Tak Terdefenisi!")
                car.FuelConsumption()
            else : 
                print("Bensin Tidak Cukup Coy")

        else:
            print("Hidupkan Dulu Mesin Nya Bang")



    def PushEnergy(self):
        print("Menu Istirahat")
        print("1.Sleep \n2. Eating")
        Pilihan = int(input("Masukan Pilihan Istirahat :"))
        if Pilihan == 1:
            self.energy += 5
        elif Pilihan == 2:
            self.energy += 15
            self.cash -= 10
        else:
            print("Invalid Menu!")
    