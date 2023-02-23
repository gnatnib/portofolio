# Nama file: 1.pengurangan.py
# Pembuat  : Bintang Syafrian Rizal - 24060122120031
# Tanggal  : 29 September 2022
# Deskripsi: Membuat fungsi-fungsi operasi dalam matematika dngan menggunakan rekursi

# Definisi dan Spesifikasi
# pengurangan : 2 interger --> interger
# { pengurangan (a,b) mengurangkan dua buah bilangan interger yaitu a dengan b.}

# Realisasi 
def pengurangan(x,y):
    if y ==0:
        return x
    else:
        return pengurangan (x,y-1) -1

# Aplikasi
print (pengurangan(8,4))
# pengurangan (8,3) -1
# pengurangan (8,2) -1 -1 
# pengurangan (8,1) -1 -1 -1
# pengurangan (8,0) -1 -1 -1 -1