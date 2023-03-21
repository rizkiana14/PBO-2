class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def berbicara(self):
        print(f"{self.nama} sedang presentasi.")
class mahasiswa(Manusia):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)
        self.nim= nim
    def menjelaskan(self):
        print(f"{self.nama} dengan NIM {self.nim} sedang menjelaskan.")
mahasiswaA = mahasiswa("kia", 25, "210511080")
mahasiswaA.berbicara() # Output: kia sedang presentasi.
mahasiswaA.menjelaskan() # Output:kia dengan NIM 210511080 sedang menjelaskan.