# Kelas Induk
class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def bergerak(self):
        return f"{self.nama} sedang bergerak."

# Kelas Anak (Inheritance)
class Burung(Hewan):
    def __init__(self, nama, umur, jenis_burung):
        # Memanggil konstruktor dari kelas induk
        super().__init__(nama, umur)
        self.jenis_burung = jenis_burung
    
    def terbang(self):
        return f"{self.nama} yang berjenis {self.jenis_burung} sedang terbang."
    
    # Overriding method dari kelas induk
    def bergerak(self):
        return f"{self.nama} sedang terbang di langit."

#kelas Anak (Inheritance 2)
class Ikan(Hewan):
    def __init__(self, nama, umur, jenis_ikan):
        super().__init__(nama, umur)
        self.jenis_ikan = jenis_ikan
        
    def berenang(self):
        return f"{self.nama} berjenis {self.jenis_ikan} sedang berenang"    
    
    def bergerak(self):
        return f"{self.nama} sedang berenang di sungai."

# Contoh Penggunaan
hewan1 = Hewan("Kucing", 3)
print(hewan1.bergerak())  # Output: Kucing sedang bergerak.

burung1 = Burung("Elang", 5, "Elang Emas")
print(burung1.bergerak())  # Output: Elang sedang terbang di langit.
print(burung1.terbang())   # Output: Elang yang berjenis Elang Emas sedang terbang.

ikan1 = Ikan("Arwana", 2, "Arwana Hitam")
print(ikan1.bergerak())
print(ikan1.berenang())

#nambah ini deh