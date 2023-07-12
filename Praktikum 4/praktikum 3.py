class Penulis:
    def __init__(self, nama_penulis):
        self.nama_penulis = nama_penulis
        self.daftar_buku = []
    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

class Buku:
    def __init__(self, judul_buku, tahun_terbit, penulis):
        self.judul_buku = judul_buku
        self.tahun_terbit = tahun_terbit
        self.penulis = penulis
    def tampilkan_informasi(self):
        print(f"Judul: {self.judul_buku}")
        print(f"Tahun Terbit: {self.tahun_terbit}")
        print(f"Penulis: {self.penulis.nama_penulis}")

penulis1 = Penulis("J.K. Rowling")
penulis2 = Penulis("Jane Austen")
penulis3 = Penulis("Nicholas Sparks")

buku1 = Buku("Harry Potter and the Philosopher's Stone", 1997, penulis1)
buku2 = Buku("Harry Potter and the Chamber of Secrets", 1998, penulis1)
buku3 = Buku("Pride and Prejudice", 1813, penulis2)
buku4 = Buku("The Notebook", 1996, penulis3)

penulis1.tambah_buku(buku1)
penulis1.tambah_buku(buku2)
penulis2.tambah_buku(buku3)
penulis2.tambah_buku(buku4)

buku1.tampilkan_informasi()
buku2.tampilkan_informasi()
buku3.tampilkan_informasi()
buku4.tampilkan_informasi()
