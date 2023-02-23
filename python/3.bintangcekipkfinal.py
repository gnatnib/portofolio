# Nama file  : 3.bintangcekipk.py
# Dibuat oleh: Bintang Syafrian Rizal - NIM : 24060122120031
# Tanggal    : 2 September 2022
# Deskripsi  : Mengetahui apakah seorang mahasiswa lulus dengan predikat cumlaude berdasarkan masa studi yang dinyatakan dalam bulan
#             dan nilai IPK yang dinyatakan dengan range [0 sampai 4].

# Definisi dan Spesifikasi  
# cumlaude = 2 interger >= 0 ---> boolean
#            {cumlaude (bulan,nilai) benar jika (bulan,nilai) bulan bernilai kurang dari sama dengan 54
#             dan nilai bernilai lebih dari sama dengan 3.5 dan kurang dari sama dengan 4.}

# Realisasi
def cumlaude (bulan,nilai) :
    return (bulan <=54 and bulan >= 0 and nilai >= 3.5 and nilai <= 4)

# Aplikasi
print ("Hasilnya:" , cumlaude (55,4))