class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def bergerak(self):
        print(self.nama, "mengaum")
class Serigala(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu
    def bersuara(self):
        print("Aauu!")
SerigalaA = Serigala("Serigala", 2, "Arktik")
SerigalaA.bergerak() # output: Serigala bergerak
SerigalaA.bersuara() # output: Aauu!