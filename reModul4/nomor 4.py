class Mhs(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

h0 = Mhs("anies", 107, "Sukoharjo", 240000)
h1 = Mhs("Salsa", 113, "Sragen", 230000)
h2 = Mhs("Anggi", 145, "Surakarta", 250000)
h3 = Mhs("Tyas", 180, "Surakarta", 235000)
h4 = Mhs("Emir", 104, "Boyolali", 240000)
h5 = Mhs("Reza", 131, "Salatiga", 250000)
h6 = Mhs("Denisha", 123, "Klaten", 245000)
h7 = Mhs("daniel", 234, "bekasi", 245000)
h8 = Mhs("miwa", 213, "sunter", 245000)
h9 = Mhs("nana", 164, "atas bumi", 270000)
h10 = Mhs("Kun", 129, "Purwodadi", 265000)

Daftar = [h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10]

def cariUangSakuKurang250k(list):
    temp = []
    for i in list:
        if i.uangSaku < 250000:
            temp.append(i)
    return temp

a = cariUangSakuKurang250k(Daftar)
for i in a:
    print(i.nama)
