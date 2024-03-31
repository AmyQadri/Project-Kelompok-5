class User:
    def __init__ (self, name, age,cash, email):
        self.name = name
        self.age = age
        self.energy = 0
        self.cash = cash
        self.email = email
        self.location = (0,0)
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

    def PushEnergy(self,energy):
        self.energy += energy
        self.cash += 10
            
            
