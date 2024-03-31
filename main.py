from class1 import User
from class2 import Car
from class3 import Work

CarMe = Car("Avanza","Toyota",33)
Jelita = User("Jelita Nurwahida", 20,1000000, "Jelita@mail")
Apk = Work("Surya",443301)


Jelita.UserInfo()


CarMe.StarEngine()
Jelita.RunCarForWorking(CarMe)
Jelita.Working(Apk,CarMe)
Jelita.UserInfo()

Jelita.Working(Apk,CarMe)
Jelita.Working(Apk,CarMe)
print(f"Amount Of Work :{Jelita.AmountOfWork}")
Jelita.UserInfo()

CarMe.CheckCarInfo()