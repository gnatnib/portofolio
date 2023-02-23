# Nama file     : 9.UpahMingguan2.py
# Dibuat oleh   : Bintang Syafrian Rizal - NIM : 24060122120031
# Tanggal       : 15 September 2022
# Deskripsi     : Menghitung upah karyawan berdasarkan golongan dan jumlah jam kerjanya, jika karyawan tersebut lembur, maka upah lemburnya adalah dua kali upah normal berdasarkan
#                 golongannya.

gol = str(input("Masukkan Golongan: "))

jam = int(input())

a = (40000)
b = (50000)
c = (60000)
d = (70000)


if (gol == 'a') or (gol == 'A') :
    if (jam > 40) :
        print (1600000 + (jam-40)*2*a)
    else:
        print(a*jam)
elif (gol == 'b') or (gol == 'B') :
    if (jam > 40) :
        print (2000000 + (jam-40)*2*b)
    else:
        print(b*jam)
elif (gol == 'c') or (gol == 'C') :
    if (jam > 40) :
        print (2400000 + (jam-40)*2*c)
    else:
        print (c*jam)
elif (gol == 'd') or (gol == 'D') :
    if (jam > 40) :
        print (2800000 + (jam-40)*2*d)
    else:
        print (d*jam)
else :
    print("Error!")