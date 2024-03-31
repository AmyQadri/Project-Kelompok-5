class User:
    AmountOfWork = 0
    def __init__ (self, name, age,cash, email):
        self.name = name
        self.age = age
        self.energy = 100
        self.cash = cash
        self.email = email
        self.location = ()
        self.user_level = 0
        self.reward_point = 0


    def UserInfo(self):
        print(f"Name : {self.name} \nAge : {self.age} \nEnergy : {self.energy} \nCash : {self.cash} \nEmail : {self.email} \nUser_level : {self.user_level} \nReward_point : {self.reward_point} \nLocation : {self.location}m")


    def Working(self,Apk,CarMe):
        print("Tentukan Titik Penjemputan")
        Apk.PickUp()
        print("Tentukan Titik Tujuan")
        Apk.DropOff()
        print("Jarak Yang Akan Ditempuh Adalah :",Apk.Distance())
        if self.energy > 0:
            if Apk.distance >= 100 :
                Apk.cosh = 10000
                self.cash += 10000 - 1000
                self.reward_point += 10
            elif Apk.distance >= 50 :
                Apk.cosh = 5000
                self.cash += 5000 - 1000
                self.reward_point += 5
            elif Apk.distance >= 20 :
                Apk.cosh = 3000
                self.cash += 3000 - 1000
                self.reward_point += 3
            elif Apk.distance >= 10 :
                Apk.cosh = 2000
                self.cash += 2000 - 1000
                self.reward_point += 2
            else :
                Apk.cosh = 1000
            self.energy -= 3
            self.AmountOfWork += 1
            if self.AmountOfWork >= 2 :
                self.user_level  += 1
            else:
                pass
        else:
            print("Energy Tidak Cukup")
        CarMe.FuelConsumption()
        print("Biaya Yang Harus Dibayarkan : ",Apk.cosh)

    def RunCarForWorking(self,car):
        if car.status_engine == True :
            if self.energy  > 0 :
                speed = int(input("Masukan Speed :"))
                car.Accelerate(speed)
                if speed >= 10 <= 20 :
                    self.location += 1000,2000
                elif speed >= 20 <= 50 :
                    self.location += 2000,3000
                elif speed >= 50 <= 100 :
                    self.location += 3000,4000
                else:
                    print("Lokasi Terlalu Jauh, Tak Terdefenisi!")
            else : 
                print("Energy Tidak Cukup")
        else:
            print("Hidupkan Dulu Mesin Nya Bang")



    def PushEnergy(self,energy):
        print("Reast Menu")
        print("1.Sleep \n2. Eating")
        self.energy += energy
        self.cash -= 10
    