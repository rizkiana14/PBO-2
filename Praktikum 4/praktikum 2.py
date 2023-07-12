class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.kelompok = None
    def gabung_kelompok(self, kelompok):
        self.kelompok = kelompok
        kelompok.tambah_anggota(self)
        
class KelompokKKM:
    def __init__(self, nomor):
        self.nomor = nomor
        self.anggota = []
    def tambah_anggota(self, mahasiswa):
        self.anggota.append(mahasiswa)
    def __str__(self):
        return f"Kelompok KKM {self.nomor} dengan anggota: {[mhs.nama for mhs in self.anggota]}"


mhs1 = Mahasiswa("Linda", "2105098")
mhs2 = Mahasiswa("Julian", "2105076")
mhs3 = Mahasiswa("Billy", "2105054")
mhs4 = Mahasiswa("Edzwar", "2105032")
mhs5 = Mahasiswa("Novita", "2105010")

kelompok1 = KelompokKKM(1)
kelompok2 = KelompokKKM(2)

mhs1.gabung_kelompok(kelompok1)
mhs2.gabung_kelompok(kelompok1)
mhs3.gabung_kelompok(kelompok2)
mhs4.gabung_kelompok(kelompok2)
mhs5.gabung_kelompok(kelompok2)

print(kelompok1)
print(kelompok2)
