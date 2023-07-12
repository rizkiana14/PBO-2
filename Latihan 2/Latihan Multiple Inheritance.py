# LINDA NOVITA JULIYANTI
# 210510003
# D3

class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")

class Pekerja:
    def __init__(self, pekerjaan, gaji):
        self.pekerjaan = pekerjaan
        self.gaji = gaji
    def display_info(self):
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Gaji: {self.gaji}")

class Freelance:
    def __init__(self, designgraphic):
        self.design = designgraphic
    def display_info(self):
        print(f"Design: {self.design}")

class FreelancePekerja(Orang, Pekerja, Freelance):
    def __init__(self, nama, umur, pekerjaan, gaji, designgraphic):
        Orang.__init__(self, nama, umur)
        Pekerja.__init__(self, pekerjaan, gaji)
        Freelance.__init__(self, designgraphic)
    def display_info(self):
        super().display_info()
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Gaji: {self.gaji}")
        print(f"Bagian: {self.design}")
    
FreelancePekerja = FreelancePekerja("Bennedeta", 25, "Freelance", "$5000", "Design Graphic")
FreelancePekerja.display_info()
