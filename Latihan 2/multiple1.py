class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def presentasi(self):
        print(self.nama, "sedang belajar")
class Pekerja:
    def __init__(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan
    def bekerja(self):
        print(self.nama, "sedang bekerja")
class MahasiswaPekerja(Mahasiswa, Pekerja):
    def __init__(self, nama, nim, pekerjaan):
        Mahasiswa.__init__(self, nama, nim)
        Pekerja.__init__(self, nama, pekerjaan)
    def bersosialisasi(self):
        print(self.nama, "sedang belajar di rumah")
mhs_pekerja = MahasiswaPekerja("kia", "210511080", "belajar")
mhs_pekerja.presentasi() # output: kia sedang belajar
mhs_pekerja.presentasi() # output: kia sedang belajar
mhs_pekerja.bersosialisasi() # output: kia sedang bersosialisasi