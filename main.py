import class1
import class2
import class3


class Sekolah:
    def __init__ (self,nilai, sks, kls):
        self.nilai = nilai
        self.sks = sks
        self.kls = kls

    def __str__(self):
        return "Nilai: {}\nSKS: {}\nKelas: {}".format(self.nilai, self.sks, self.kls)
    