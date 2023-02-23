# Nama file     : NextTime.py
# Dibuat oleh   : Bintang Syafrian Rizal - NIM : 24060122120031
# Tanggal       : 15 September 2022
# Deskripsi     : Mengetahui jam, menit, dan satu detik setelahnya dari input jam, menit, dan satu detik yang diinput.


a = int(input())
b = int(input())
c = int(input())

if (a<24) and (a>0) and (b<60) and (b>=0) and (c<60) and (c>=0):
        
    if (c==59) :
        if (a==23) and (b==59):
            print ("00 : 00 : 00")
        elif (b==59):
            print (a+1,": 00 : 00")
        else:
            print (a,":",b+1,":","00")
    else:
        print (a,":",b,":",c+1)
else:
    print ("Invalid!")