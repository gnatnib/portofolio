# Nama file  : 3.bintangcekipk.py
# Dibuat oleh: Bintang Syafrian Rizal - NIM : 24060122120031
# Tanggal    : 2 September 2022
# Deskripsi  : Mengetahui apakah seorang mahasiswa lulus dengan predikat cumlaude berdasarkan masa studi yang dinyatakan dalam bulan
#             dan nilai IPK yang dinyatakan dengan range [0 sampai 4].

# Definisi dan Spesifikasi  
# cumlaude = 2 interger >= 0 ---> boolean
#            {cumlaude (tahun,nilaiipk) benar jika (tahun,nilaiipk) tahun bernilai kurang dari sama dengan 54
#             dan nilaiipk bernilai lebih dari sama dengan 3.5 dan kurang dari sama dengan 4.}

# Realisasi
def cumlaude (bulan,nilaiipk) :
    if (nilaiipk > 4) or (nilaiipk < 0) :
        print ("Nilai yang anda masukkan tidak valid.")
    elif (bulan <= 54) and (nilaiipk >= 3.5) and (nilaiipk <= 4) :
        print ("Anda lulus dengan predikat cumlaude.")
    else :
        print ("Mohon maaf, anda tidak lulus dengan predikat cumlaude.")

# Aplikasi
cumlaude (51,3.6)
    