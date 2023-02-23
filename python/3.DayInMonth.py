# Nama file     : 3.DayInMonth.pb
# Dibuat oleh   : Bintang Syafrian Rizal - NIM : 24060122120031
# Tanggal       : 15 September 2022
# Deskripsi     : Mengetahui jumlah hari dalam sebulan dengan menginput nomor bulan dan tahun, tahun perlu dicek apakah kabisat atau bukan.

b = int(input("Masukkan Bulan: "))
t = int(input("Masukkan Tahun: "))

if (b==1)or(b==3)or(b==5)or(b==7)or(b==8)or(b==10)or(b==12) :
    print("31")
    
elif (b==2):
    if (t%400 ==0) or (t%4 ==0) and (t%100 != 0) :
        print ("29")
    else :
        print("28")

else :
    print("30")
        