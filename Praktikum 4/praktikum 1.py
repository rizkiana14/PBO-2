class Peneliti:
    def __init__(self, nama):
        self.nama = nama
        self.jurnals = []
        
    def tambah_jurnal(self, judul, penulis, tahun_terbit):
        jurnal = Jurnal(judul, penulis, tahun_terbit)
        self.jurnals.append(jurnal) 
    def __str__(self):
        return f'Peneliti : {self.nama}'
        
class Jurnal:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
    def __str__(self):
        return f'{self.judul}, {self.penulis}, {self.tahun_terbit}'

peneliti1 = Peneliti('Jurnal Penelitian Teknik Informatika')
peneliti1.tambah_jurnal('ARSITEKTURAL DAN PEMROSESAN JARINGAN MENGGUNAKAN AGEN CERDAS MOBILE', 'Sri Yulianto J.P.M, Silvia Rostianingsih', 2005)
peneliti1.tambah_jurnal('Uji Kelayakan Implementasi SSH sebagai Pengaman FTP Server dengan Penetration Testing', 'Batara Sakti, Abdul Aziz, Afrizal Doewes', 2013)

print(peneliti1)
for jurnal in peneliti1.jurnals:
    print(jurnal)
