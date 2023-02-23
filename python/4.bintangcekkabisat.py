# Nama file  : 4.bintangcekkabisat.py
# Dibuat oleh: Bintang Syafrian Rizal - NIM : 24060122120031
# Tanggal    : 2 September 2022
# Deskripsi  : Mengetahui apakah sebuah tahun merupakan tahun kabisat atau bukan dengan syarat angka tahun habis dibagi 400
#              atau angka tahun habis dibagi 4, tetapi tidak habis dibagi 100.

# Definisi dan Spesifikasi
# kabisat = interger >= 0 ----> boolean
#           {kabisat (tahun) benar apabila (tahun) merupakan angka yang habis dibagi 400 atau angka yang habis dibagi 4,
#            tetapi tidak habis dibagi 100.}

# Realisasi
def kabisat (tahun):
    return (tahun % 400 == 0 or tahun % 4 == 0 and tahun % 100 != 0)

# Aplikasi
print (kabisat (2005))