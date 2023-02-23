# Nama file : garis.py
# Pembuat   : Bintang Syafrian Rizal - 24060122120031
#             Surya Fajar - 24060122140107
#             Syariful Hanif Setiawan - 24060122130095
#             Fikri Azka Pradya - 24060122140171
# Tanggal   : 30 September 2022
# Deskripsi : membuat tipe bentukan garis dan point beserta konstruktor, selektor, operator, dan predikatnya.

# Definisi Type
# Type pecahanc: <bil: interger, n: interger, d: interger>
# {bil adalah bilangan bulat pecahan campuran, n adalah pembilang pecahan campuran, d adalah penyebut pecahan campuran,
#  penyebut tidak boleh nol dan pembilang harus selalu lebih besar dari penyebut.}
# Type pecahan: < pemb: interger, peny: interger.>
# { pemb adalah pembilang, peny adalah penyebut, penyebut tidak boleh nol.}

# Definisi dan Spesifikasi Konstruktor
# MakePecahanc: 3 interger --> pecahanc
# MakePecahanc (bil, n , d) membentuk sebuah pecahan campuran dengan bil sebagai bilangan bulat pecahan campuran,
# n sebagai pembilang, dan d sebagai penyebut.

# MakePecahan: 2 interger --> pecahan
# MakePecahan (pemb, peny) membentuk sebuah pecahan dengan pemb sebagai pembilang, dan peny sebagai penyebut

# Realisasi
def MakePecahanc(bil,n,d):
    return [bil,n,d]

def MakePecahan (pemb,peny):
    return [pemb,peny]

# Definisi dan Spesifikasi Selektor
# bil: pecahanc --> interger
# bil(P) memberikan bilangan bulat pecahan campuran P

# n: pecahanc --> interger
# n(P) memberikan pembilang dari pecahan campuran P

# d: pecahanc --> interger
# d(P) memberikan penyebut dari pecahan campuran P

# pemb: pecahan --> interger
# pemb(P) memberikan pembilang dari pecahan biasa P

#peny: pecahan --> interger
# peny(P) memberikan penyebut dari pecahan biasa P

# Realisasi
def bil(P):
    return P[0]

def n(P):
    return P[1]

def d(P):
    return P[2]

def pemb(P):
    return P[0]

def peny(P):
    return P[1]

# Definisi dan Spesifikasi Operator
# KonversiPecahan: pecahanc --> pecahan
# KonversiPecahan(P) mengubah pecahan campuran P ke pecahan biasa

# KonversiReal: pecahanc --> real
# KonversiReal(P) mengubah pecahan campuran P ke nilai real

# AddP: 2 pecahanc --> pecahanc
# AddP(P1, P2) menjumlahkan pecahan campuran P1 dan P2

# SubP: 2 pecahanc --> pecahanc
# SubP(P1, P2) mengurangkan pecahan campuran P1 dan P2

# DivP: 2 pecahanc --> pecahanc
# DivP(P1, P2) membagi pecahan campuran P1 dan P2

# MulP: 2 pecahanc --> pecahanc
# MulP(P1, P2) mengalikan pecahan campuran P1 dan P2

# Realisasi
def KonversiPecahan(P):
    if bil(P) >= 0:
        return MakePecahan(bil(P)* d(P) + n(P), d(P))
    else:
        return MakePecahan(bil(P)*d(P)-n(P), d(P))

def KonversiReal(P):
    if bil (P) >= 0:
        return bil(P) + (n(P)/d(P))
    else:
        return bil(P) - (n(P)/d(P))

def AddP(P1,P2):
    return (pemb(P1)*peny(P2))+(pemb(P2)*peny(P1)),(peny(P1)*peny(P2))
def SubP(P1,P2):
    return (pemb(P1)*peny(P2))-(pemb(P2)*peny(P1)),(peny(P1)*peny(P2))
def MulP(P1,P2) :
    return pemb(P1)*pemb(P2),peny(P1)*peny(P2)
def DivP(P1,P2) :
    return pemb(P1)*peny(P2),peny(P1)*pemb(P2)

def isequal(P1,P2):
    return pemb(P1)*peny(P2)==pemb(P2)*peny(P1)
def isltp(P1,P2):
    return pemb(P1)*peny(P2)<pemb(P2)*peny(P1)
def isgtp(P1,P2):
    return pemb(P1)*peny(P2)>pemb(P2)*peny(P1)




# Aplikasi
print (KonversiReal(MakePecahanc(-7,2,5)))
print (KonversiPecahan(MakePecahanc(-7,2,5)))
print (AddP(KonversiPecahan(MakePecahanc(-4,1,2)),KonversiPecahan(MakePecahanc(-2,1,3))))
print (DivP(KonversiPecahan(MakePecahanc(-3,4,5)),KonversiPecahan(MakePecahanc(1,1,2))))
print (isgtp(KonversiPecahan(MakePecahanc(1,1,5)),KonversiPecahan(MakePecahanc(-3,4,5))))
