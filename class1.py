class User:
    def __init__ (self, name, age, energy, cash, email, user_level, reward_point):
        self.name = name
        self.age = age
        self.energy = energy
        self.cash = cash
        self.email = email
        self.location = location
        self.user_level = user_level
        self.reward_point = reward_point

    def user_info(self):
        print(f"Name : {self.name} \nAge : {self.age} \nEnergy : {self.cash} \nCash : {self.cash} \nEmail : {self.email} \nUser_level : {self.user_level} \nReward_point : {self.reward_point}")

surya = User("surya", 29, 80, 1000000, "surya@mail", 5, 10)

    