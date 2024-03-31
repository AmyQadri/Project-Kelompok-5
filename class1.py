class User:
    def __init__ (self, name, age,cash, email):
        self.name = name
        self.age = age
        self.energy = 0
        self.cash = cash
        self.email = email
        self.location = ()
        self.user_level = 0
        self.reward_point = 0

    def UserInfo(self):
        print(f"Name : {self.name} \nAge : {self.age} \nEnergy : {self.cash} \nCash : {self.cash} \nEmail : {self.email} \nUser_level : {self.user_level} \nReward_point : {self.reward_point} \nLocation : {self.location}m")

    def RunCarForWorking(self,car):
        if car.status_engine == True :
            speed = int(input("Masukan Speed :"))
            car.Accelerate(speed)
            if speed >= 10 <=20 :
                self.location += 1000,2000
            elif speed >= 20 <= 50 :
                self.location += 2000,3000
            elif speed >= 50 <= 100 :
                self.location += 3000,4000
            else:
                print("Lokasi Terlalu Jauh, Tak Terdefenisi!")
        else:
            print("Hidupkan Dulu Mesin Nya Bang")

    def Working(self,Apk):
        print("Tentukan Titik Penjemputan")
        Apk.PickUp()
        print("SkdjJFFKA")
        Apk.DropOff()
        print("Jarak Yang Akan Ditempuh Adalah :",Apk.Distance())
        if Apk.distance >= 100 :
            Apk.cosh = 10000
            self.reward_point += 10
        elif Apk.distance >= 50 :
            Apk.cosh = 5000
            self.reward_point += 5
        elif Apk.distance >= 20 :
            Apk.cosh = 3000
            self.reward_point += 3
        elif Apk.distance >= 10 :
            Apk.cosh = 2000
            self.reward_point += 2
        else :
            Apk.cosh = 1000
        print("Biaya Yang Harus Dibayarkan : ",Apk.cosh)
        


    def PushEnergy(self,energy):
        self.energy += energy
        self.cash += 10
            
            