from user import User
from car import Car
from application import WorkApplication

CarMe = Car("Avanza","Toyota",35)
Jelita = User("Jelita Nurwahida", 20,1000000, "Jelita@gmail.com")
Driver = WorkApplication("Jelita",443301)
Menu = 0


while Menu != 9:
    print("\n================================================")
    print("Selamat Datang! Pilih Menu Yang Ingin Dijalankan :")
    print("1. Check Informasi Pengguna")
    print("2. Check Informasi Mobil")
    print("3. Check Informasi Driver")
    print("4. Nyalakan Mesin Mobil")
    print("5. Matikan Mesin Mobil")
    print("6. Pergi Bekerja")
    print("7. Istirahat (Menambah Energy)")
    print("8. Isi Bahan Bakar")
    print("9. Exit \n")
    print("=================================================")
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
        Jelita.RunCarForWorking(CarMe)
        print("\nINFORMASI : \nTotal Point Anda Adalah :",Jelita.reward_point)
        print("Total Cash Anda Adalah :",Jelita.cash)
        print("Sisa Bensin :",CarMe.capacity)
        print("Sisa Energy :",Jelita.energy)
    elif Menu == 7:
        Jelita.PushEnergy()
        print("Sisa Cash Anda Adalah :",Jelita.cash)
        print("Energy Saat Ini Adalah :",Jelita.energy)
    elif Menu == 8:
        CarMe.Refuel(Jelita)
        print("Total Bensin Saat Ini :",CarMe.capacity)
    elif Menu == 9:
        print("Terima Kasih Atas Kehadiran Anda!")
    else:
        print("Invalid Menu!")
        break



'''
KELOMPOK 5 ::

Iqbal
'''