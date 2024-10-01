# Kelas dasar Karyawan
class Karyawan:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok
    
    # Method untuk menghitung gaji (akan di override)
    def hitung_gaji(self):
        return self.gaji_pokok

# Karyawan Tetap: Gaji = Gaji Pokok + Tunjangan
class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan

    # Override method hitung_gaji
    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan

# Karyawan Kontrak: Gaji = Gaji Pokok + Bonus jika ada
class KaryawanKontrak(Karyawan):
    def __init__(self, nama, gaji_pokok, bonus=0):
        super().__init__(nama, gaji_pokok)
        self.bonus = bonus

    # Override method hitung_gaji
    def hitung_gaji(self):
        return self.gaji_pokok + self.bonus

# Studi Kasus
karyawan_tetap = KaryawanTetap("Budi", 5000000, 1500000)
karyawan_kontrak = KaryawanKontrak("Ani", 4000000, 500000)

print(f"Gaji {karyawan_tetap.nama}  : Rp {karyawan_tetap.hitung_gaji()}")
# Output: Gaji Budi: Rp 6500000

print(f"Gaji {karyawan_kontrak.nama}   : Rp {karyawan_kontrak.hitung_gaji()}")
# Output: Gaji Ani: Rp 4500000
