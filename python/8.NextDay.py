# Nama file     : 8.NextDay.py
# Dibuat oleh   : Bintang Syafrian Rizal - NIM : 24060122120031
# Tanggal       : 15 September 2022
# Deskripsi     : Mengetahui hari, bulan, tahun pada 1 hari berikutnya dari hari, bulan, tahun yang diinput sebelumnya.

hari = int(input())
bulan = int(input())
tahun = int (input())

if (hari>0) and (hari<=31) and (bulan<=12) and (bulan>0) and ((bulan==1)or(bulan==3)or(bulan==5)or(bulan==7)or(bulan==8)or(bulan==10)or(bulan==12)):
    if (hari==31):
        if (bulan==12):
            print((1,1,tahun+1))
        else:
            print ((1, bulan+1, tahun))
    else :
        print ((hari+1, bulan, tahun))
elif (hari<31) and (hari>0) and (bulan<=12) and (bulan>0) and ((bulan==4)or(bulan==6)or(bulan==9)or(bulan==11)) :
    if (hari==30):
        if (bulan==12):
            print((1,1,tahun+1))
        else:    
            print ((1, bulan+1, tahun))
    else :
        print ((hari+1, bulan, tahun))
elif (hari<=29) and (hari>0) and (bulan==2) and ((tahun%4==0) or (tahun%400==0) and (tahun %100 !=0)):
    if (hari==29):
        print ((1,bulan+1,tahun))
    else:
        print((hari+1,bulan,tahun))
elif (hari<=28) and (hari>0) and (bulan==2) and ((tahun%4!=0) or (tahun%400!=0) and (tahun %100 ==0)):
    if (hari==28):
        print ((1,bulan+1,tahun))
    elif (hari <28):
        print((hari+1,bulan,tahun))
    else:
        print ("Error!")
else:
    print ("Error!")
    