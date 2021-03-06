class Mhs(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

h0 = Mhs("Aini", 107, "Sukoharjo", 240000)
h1 = Mhs("Salsa", 113, "Sragen", 230000)
h2 = Mhs("Anggi", 145, "Surakarta", 250000)
h3 = Mhs("Tyas", 180, "Surakarta", 235000)
h4 = Mhs("Eko", 104, "Boyolali", 240000)
h5 = Mhs("Reza", 131, "Salatiga", 250000)
h6 = Mhs("Denis", 123, "Klaten", 245000)
h7 = Mhs("Udin", 234, "Wonogiri", 245000)
h8 = Mhs("Dandung", 213, "Klaten", 245000)
h9 = Mhs("Hasna", 164, "Karanganyar", 270000)
h10 = Mhs("Kun", 129, "Purwodadi", 265000)

Daftar = [h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10]

def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan)-1
    while low <= high:
        mid = (high+low)//2
        if kumpulan[mid] == target:
            return mid
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

kumpulan = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
print(binSe(kumpulan, 5))
