# Nama file : Waktuu.py
# Pembuat   : Bintang Syafrian Rizal - 24060122120031
#             Surya Fajar - 24060122140107
#             Syariful Hanif Setiawan - 24060122130095
#             Fikri Azka Pradya - 24060122140171
# Tanggal   : 02 Oktober 2022
# Deskripsi : membuat tipe bentukan waktu beserta konstruktor, selektor, operator, dan predikatnya.

# DEFINISI DAN SPESIFIKASI TYPE
# type Hour : integer [0...23]
#   {definisi ini hanyalah untuk “menamakan” type integer dengan nilai tertentu supaya
#   mewakili jam }
# type Minute : integer [0...59]
#   {definisi ini hanyalah untuk “menamakan” type integer dengan daerah nilai tertentu
#   supaya mewakili menit }
# type Second : integer [0...59]
#   {definisi ini hanyalah untuk “menamakan“ type integer dengan daerah nilai tertentu
#   supaya mewakili detik }
# type time <h:jam,m:menit,s:detik>
#   { <h,m,s> adalah jam h menit m detik s }

# DEFINISI DAN SPESIFIKASI TYPE KONSTRUKTOR
# MakeTime: <jam,menit,detik> -> time
#   {MakeTime<h,m,s>-> waktu pada jam,menit,detik yang bersangkutan}
# Realisasi
def Time(h, m, s):
    return [h, m, s]

# DEFINISI DAN SPESIFIKASI SELEKTOR
#  Second : Time → detik
#   {Second (D) memberikan detik s dari S yang terdiri dari <h,m,s> }
# Realisasi
def Hour(S):
    return S [0]

def Minute(S):
    return S [1]

def Second(S):
    return S [2]

# DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI LAIN TERHADAP TIME
# PreviousTime : Time → Time
#  { PreviousTime(S): Menghitung Time yang merupakan 1 hari sebelum Time S yang
#   diberikan}
# Realisasi
def PreviousTime(S):
    if Hour(S) == 0 and Minute(S) != 0 and Second(S) != 0:
        return (23, Minute(S), Second(S))
    elif Hour(S) != 0 and Minute(S) == 0 and Second(S) != 0:
        return (Hour(S)-1,59,Second(S))
    elif Hour(S) != 0 and Minute(S) != 0 and Second(S) == 0:
        return (Hour(S),Minute(S)-1,59)
    elif Hour(S) != 0 and Minute(S) == 0 and Second(S) == 0:
        return (Hour(S)-1,59,59)
    elif Hour(S) == 0 and Minute(S) == 0 and Second(S) == 0:
        return (23,59,59)
    else:
        return (Hour(S),Minute(S),Second(S)-1)

# NextTime : Time → Time
#  { NextTime(S): Menghitung Time yang merupakan 1 hari setelah Time S yang
#   diberikan}
# Realisasi
def NextTime(S):
    if Hour(S) == 23 and Minute(S) != 59 and Second(S) != 59:
        return (0, Minute(S), Second(S))
    elif Hour(S) != 23 and Minute(S) == 59 and Second(S) != 59:
        return (Hour(S)+1,1,Second(S))
    elif Hour(S) != 23 and Minute(S) != 59 and Second(S) == 59:
        return (Hour(S),Minute(S)+1,1)
    elif Hour(S) != 23 and Minute(S) == 59 and Second(S) == 59:
        return (Hour(S)+1,0,0)
    elif Hour(S) == 23 and Minute(S) == 59 and Second(S) == 59:
        return (0,0,0)
    else:
        return (Hour(S),Minute(S),Second(S)+1)
    
# konversi_detik : Time -> integer
#  { konversi_detik(S): Menjumlah Time menjadi detik}
# Realisasi
def konversi_detik(S):
    return Hour(S)*3600 + Minute(S)*60 + Second(S)

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEqD?: 2 Time → boolean
#  {IsEqD?(S1,S2) benar jika S1=S2, mengirimkan true jika h1=h2 and m1=m2 and s1=s2}
# Realisasi
def IsEqD(S1,S2):
    return konversi_detik(S1) == konversi_detik(S2) and Hour(S1)== Hour(S2) and Minute(S1)==Minute(S2) and Second(S1)==Second(S2)

# IsBefore? : 2 Time → boolean
#  {IsBefore?(S1,S2) benar jika S1 adalah sebelum S2 mengirimkan true jika S1 adalah
#   "sebelum" S2}
# Realisasi
def IsBefore(S1,S2):
    return konversi_detik(S1) < konversi_detik(S2)

# IsAfter? : 2 Time → boolean
#  {IsAfter?(S1,S2) benar jika S1 adalah sesudah S2 mengirimkan true jika S1 adalah
#   "sesudah" S2: konversi_detik dari S1 adalah lebih besar dari konversi_detik dari S2.}
# Realisasi
def IsAfter(S1,S2):
    return konversi_detik(S1) > konversi_detik(S2)


print(PreviousTime(Time(2,5,7)))
print(NextTime(Time(5,0,59)))
print(konversi_detik(Time(2,2,2)))
print(IsEqD(Time(2, 2, 2), Time(2, 3, 2)))
print(IsBefore(Time(2, 2, 2), Time(2, 3, 2)))
print(IsAfter(Time(2, 2, 2), Time(2, 3, 2)))


        