# Kelas dasar (parent class)
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        return "Hewan ini mengeluarkan suara."

# Kelas turunan (child class)
class Anjing(Hewan):
    def __init__(self, nama, ras):
        super().__init__(nama)
        self.ras = ras

    def suara(self):
        return "Anjing menggonggong: Woof! Woof!"

# Kelas turunan lainnya
class Kucing(Hewan):
    def __init__(self, nama, warna):
        super().__init__(nama)
        self.warna = warna

    def suara(self):
        return "Kucing mengeong: Meow! Meow!"
    
    # Kelas turunan lainnya
class Bebek(Hewan):
    def __init__(self, nama, warna):
        super().__init__(nama)
        self.warna = warna

    def suara(self):
        return "Bebek kwekkwek: Kwek! Kwek!"

# Membuat objek dari kelas Anjing dan Kucing
anjing1 = Anjing("Buddy", "Golden Retriever")
kucing1 = Kucing("Milo", "Putih")
bebek1 = Bebek("yepo", "hitam")

# Menggunakan metode dan atribut
print(f"{anjing1.nama} adalah seekor {anjing1.ras} dan suaranya: {anjing1.suara()}")
print(f"{kucing1.nama} adalah kucing berwarna {kucing1.warna} dan suaranya: {kucing1.suara()}")
print(f"{bebek1.nama} adalah bebek berwarna {bebek1.warna} dan suaranya: {bebek1.suara()}")