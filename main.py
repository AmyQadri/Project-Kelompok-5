from class1 import User
from class2 import Car
from class3 import WorkApplication

CarMe = Car("Avanza","Toyota",35)
Jelita = User("Jelita Nurwahida", 20,1000000, "Jelita@gmail.com")
Driver = WorkApplication("Jelita",443301)
Menu = 0


while Menu != 10:
    print("===============================================")
    print("Selamat Datang! Pilih Menu Yang Ingin Dijalankan :")
    print("1. Check Informasi Pengguna")
    print("2. Check Informasi Mobil")
    print("3. Check Informasi Driver")
    print("4. Nyalakan Mesin Mobil")
    print("5. Matikan Mesin Mobil")
    print("6. Jalankan Aplikasi")
    print("7. Jalankan Mobil")
    print("8. Istirahat (Menambah Energy)")
    print("9. Isi Bahan Bakar")
    print("10. Exit")
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
        CarMe.Refuel()
    elif Menu == 10:
        print("Terima Kasih Atas Kehadiran Anda!")
    else:
        print("Invalid Menu!")
        break
