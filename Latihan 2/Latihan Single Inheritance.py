# LINDA NOVITA JULIYANTI
# 210510003
# D3

class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def bertanya(self):
        print(f"{self.nama} sedang bertanya.")

class Mahasiswa(Manusia):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)
        self.nim = nim
    def mengikutikelas(self):
        print(f"{self.nama} dengan NIM {self.nim} sedang mengikuti kelas.")

mahasiswa = Mahasiswa("Linda", 21, "210510003")
mahasiswa.bertanya()
mahasiswa.mengikutikelas()
