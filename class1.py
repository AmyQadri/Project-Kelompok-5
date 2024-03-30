class User:
    def __init__ (self, name, age, energy, cash, email, user_level, reward_point):
        self.name = name
        self.age = age
        self.energy = energy
        self.cash = cash
        self.email = email
        self.location = ()
        self.user_level = user_level
        self.reward_point = reward_point

    def user_info(self):
        print(f"Name : {self.name} \nAge : {self.age} \nEnergy : {self.cash} \nCash : {self.cash} \nEmail : {self.email} \nUser_level : {self.user_level} \nReward_point : {self.reward_point} \nLocation : {self.location}m")

    def Working(self,car):
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
            
            
