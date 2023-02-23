#Nama file  : pecahan.py
#Deskripsi  : Membuat tipe bentukan pecahan beserta konstruktor dan selektornya
#Pembuat    : Bintang Syafrian Rizal 24060122120031
#Tanggal    :20 September 2022

from math import sqrt

#DEFINISI TYPE
#Type pecahan : <n:interger>=0,d:interger>0>
#{<n:interger >- 0, d:interger>0> n adalah pembilang(numerator) dan d adalah penyebut (denumerator.
#Penyebut sebuah pecahan tidak boleh nol }

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
#MakeP: interger>=0, interger>0 --> pecahan
#{ Make P(x,y) membentuk sebuah pecahan dari pembilang x dan penyebut y,
# dengan x dan y interger}

class Pecahan:
    def __init__(self,pembilang,penyebut):
        self.x = pembilang
        self.y = penyebut

#DEFINISI DAN SPESIFIKASI SELEKTOR
#Pemb : pecahan --> interger>=0
#{ Pemb(p) memberikan numerator pembilang n dari pecahan tsb }
#Realisasi dalam Python
def pemb(P) :
    return P.x

#Peny : pecahan --> interger>0
#{ Peny(p) memberikan denumerator penyebut d dari pecahan tsb }
#Realisasi dalam Python
def peny(P):
    return P.y

#DEFINISI DAN SPESIFIKASI PREDIKAT
#IsEqP? : 2 pecahan --> boolean
#{IsEqP?(p1,p2) true jika p1 = p2
#Membandingkan apakah dua buah pecahan samanilainya: n1/d1 = n2/d2 jika dan
#hanya jika n1d2=n2d1 }
def iseq(P1,P2):
    return ((pemb(P1)*peny(P2)) == (pemb(P2)*peny(P1)))

#IsLtP? : 2 pecahan --> boolean
#{IsLtP?(p1,p2) true jika p1 < p2
#Membandingkan dua buah pecahan, apakah p1 lebih kecil nilainya dari p2: n1/d1 <
#n2/d2 jika dan hanya jika n1d2 < n2d1 }
def islt(P1,P2):
    return ((pemb(P1)*peny(P2) < pemb(P2)*peny(P1)))

#IsGtP? : 2 pecahan --> boolean
#{IsGtP?(p1,p2) true jika p1 > p2
#Membandingkan nilai dua buah pecahan,, apakah p1 lebih besar nilainya dari p2:
#n1/d1 > n2/d2 jika dan hanya jika n1d2 > n2d1 }
def isgt(P1,P2):
    return ((pemb(P1)*peny(P2)) > (pemb(P2)*peny(P1))) 

#DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI LAIN TERHADAP POINT
#AddP : 2 pecahan --> pecahan
#{ AddP(P1,P2) : Menambahkan dua buah pecahan P1 dan P2 :
#n1/d1 + n2/d2 = (n1*d2 + n2*d1)/d1*d2 } 
def add(P1,P2):
    return (((pemb(P1)*peny(P2)) + (pemb(P2)*peny(P1))) / (peny(P1))*(peny(P2)))

#SubP : 2 pecahan --> pecahan
#{ SubP(P1,P2) : Mengurangkan dua buah pecahan P1 dan P2
#Mengurangkan dua pecahan : n1/d1 - n2/d2 = (n1*d2 - n2*d1)/d1*d2 } 
def sub(P1,P2):
    return (((pemb(P1)*peny(P2)) - (pemb(P2) * peny(P1))) / (peny(P1))*peny(P2))

#MulP : 2 pecahan --> pecahan
#{ MulP(P1,P2) : Mengalikan dua buah pecahan P1 dan P2
#Mengalikan dua pecahan : n1/d1 * n2/d2 = n1*n2/d1*d2 }
def mul(P1,P2):
    return ((pemb(P1)*pemb(P2)) / (peny(P1)*peny(P2)))
#DivP : 2 pecahan --> pecahan
#{ DivP(P1,P2) : Membagi dua buah pecahan P1 dan P2
#Membagi dua pecahan : (n1/d1)/(n2/d2) = n1*d2/d1*n2 } 
def div(P1,P2):
    return ((pemb(P1)*peny(P2)) / (peny(P1)*pemb(P2)))

#RealP : 2 pecahan --> pecahan
#{Menuliskan bilangan pecahan dalam notasi desimal}
def real(P):
    return (pemb(P) / peny(P))

P1 = Pecahan (2,6)
P2 = Pecahan (3,9)
print (add(P1,P2))
print (sub(P1,P2))
print (mul(P1,P2))
print (div(P1,P2))
print (real(P1))
print (iseq(P1,P2))
print (islt(P1,P2))
print (isgt(P1,P2))