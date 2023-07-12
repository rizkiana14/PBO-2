# LINDA NOVITA JULIYANTI
# 210510003
# D3

class Pakaian:
    def __init__(self, jenis, warna, size):
        self.jenis = jenis
        self.warna = warna
        self.size = size
    def get_jenis(self):
        return self.jenis
    def get_size(self):
        return self.size
    def get_warna(self):
        return self.warna

class Baju(Pakaian):
    def __init__(self, jenis, warna, size):
        super().__init__(jenis, warna, size)
        self.size = size
    def get_size(self):
        return self.size
    
class Celana(Pakaian):
    def __init__(self, jenis, warna, size):
        super().__init__(jenis, warna, size)
        self.size = size
    def get_size(self):
        return self.size

# turunan Hierarchical Inheritance
class Kemeja(Pakaian):
    def __init__(self, jenis, warna, size):
        super().__init__(jenis, warna, size)
        self.size = size
    def get_details(self):
        print(f"Jenis Baju : {self.jenis}")
        print(f"Warna : {self.warna}")
        print(f"Size: {self.size}")
        return self.size
    
class Jeans(Pakaian):
    def __init__(self, jenis, warna, size):
        super().__init__(jenis, warna, size)
        self.size = size
    def get_details(self):
        print(f"Jenis Celana : {self.jenis}")
        print(f"Warna : {self.warna}")
        print(f"Size: {self.size}")
        return self.size
    
baju = Kemeja("Kemeja", "Biru", "L")
baju.get_details()
celana = Jeans("Jeans", "Light Blue", "M")
celana.get_details()
