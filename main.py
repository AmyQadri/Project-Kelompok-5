from class1 import User
from class2 import Car
from class3 import WorkApplication

CarMe = Car("Avanza","Toyota",33)
Jelita = User("Jelita Nurwahida", 20,1000000, "Jelita@gmail.com")
Driver = WorkApplication("Surya",443301)

Menu = 0


while Menu != 9:
    print("===============================================")
    print("Selamat Datang! Pilih Menu Yang Ingin Dijalankan :")
    print("1. Check Informasi Pengguna")
    print("2. Check Informasi Mobil")
    print("3. Check Informasi Driver")
    print("4. Nyalakan Mesin Mobil")
    print("5. Matikan Mesin Mobil")
    print("6. Pergi Bekerja")
    print("7. Jalankan Mobil")
    print("8. Istirahat (Menambah Energy)")
    print("9. Exit")
    Menu = int(input("Masukan Pilihan ::"))

    if Menu == 1:
        Jelita.UserInfo()
    elif Menu == 2:
        CarMe.CheckCarInfo()
    elif Menu == 3:
        Driver.CheckDriverInfo()
    elif Menu == 4:
        CarMe.StarEngine()
    elif Menu == 5:
        CarMe.StopEngine()
    elif Menu == 6:
        Jelita.Working(Driver,CarMe)
    elif Menu == 7:
        Jelita.RunCarForWorking(CarMe)
    elif Menu == 8:
        Jelita.PushEnergy()
    elif Menu == 9:
        print("Terima Kasih Atas Kehadiran Anda!")
