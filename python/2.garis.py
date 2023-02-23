# Nama file : garis.py
# Pembuat   : Bintang Syafrian Rizal - 24060122120031
#             Surya Fajar - 24060122140107
#             Syariful Hanif Setiawan - 24060122130095
#             Fikri Azka Pradya - 24060122140171
# Tanggal   : 30 September 2022
# Deskripsi : membuat tipe bentukan garis dan point beserta konstruktor, selektor, operator, dan predikatnya.

# Definisi Type
# Type garis: <P1: point, P2: point>
# {P1 dan P2 adalah dua titik yang akan membangun sebuah garis.}
# Type point: <absis: real, ordinat: real>
# {Absis adalah absis dan ordinat adalah ordinat dari point tersebut.}

# Definisi dan Spesifikasi Konstruktor
# MakeLine: 2 point --> garis
# MAkeLine: (P1, P2) membentuk sebuah tipe garis dengan P1 dan P2 sebagai titik - titiknya

# MakePoint: 2 real --> point
# MakePointL (absis, ordinat) membentuk sebuah titik dengan absis dan ordinat sebagai absis dan ordinatnya

# TitikPotongX: 2 real --> point
# TitikPotongX (G) menentukan perpotongan garis (G) terhadap sumbu X.

# TitikPotongY: 2 real --> point
# TitikPotongY (G) menentukan perpotongan garis (G) terhadap sumbu Y.

# Realisasi
def MakeGaris (P1,P2):
    return [P1,P2]

def MakePoint (absis,ordinat):
    return [absis,ordinat]

def TitikPotongX(G):
    return (absis(P1(G)) - (((absis(P2(G))) - absis(P1(G))) / (ordinat(P2(G))- ordinat(P1(G))) * ordinat(P1(G)))),0

def TitikPotongY(G):
    return 0,(ordinat(P1(G)) - (((ordinat(P2(G))) - ordinat(P1(G))) /(absis(P2(G)) - absis(P1(G))) * absis(P1(G))))
# Definisi dan Spesifikasi Selektor
# P1: garis --> point
# P1(G) mengembalikan point pertama dari garis G

# P2: garis --> point
# P2(G) mengembalikan point kedua dari garis G

# absis: point --> real
# absis(P) mengembalikan point pertama dari point P

# ordinat: point --> real
# ordinat(P) mengembalikan point kedua dari point P

# Realisasi
def P1(G):
    return G[0]

def P2(G):
    return G[1]

def absis(P):
    return P[0]

def ordinat(P):
    return P[1]

# Definisi dan Spesifikasi Operator
# Gradien: garis --> real
# Gradien(G) menghitung gradien garis G

# PanjangGaris: garis --> real
# PanjangGaris(G) menghitung panjang garis G

# Realisasi
def Gradien(G):
    return (ordinat(P2(G)) - ordinat(P1(G))) / (absis(P2(G)) - absis(P1(G)))

def PanjangGaris(G):
    return (((absis(P2(G))) - absis(P1(G)))**2 + (ordinat(P2(G)) - ordinat(P1(G)))**2)**0.5

# Definisi dan Spesifikasi Predikat
# IsSejajar: 2 garis --> boolean
# IsSejajar (G1, G2) true ketika G1 sejajar dengan G2 (gradien G1 dan G2 sama)
# IsTegakLurus: 2 garis --> boolean
# IsTegakLurus (G1, G2) true ketika G1 tegak lurus dengan G2 (gradien G1 dikalikan gradien G2 sama dengan -1)

# Realisasi
def IsSejajar(G1,G2):
    return Gradien(G1) == Gradien(G2)

def IsTegakLurus(G1,G2):
    return Gradien(G1) * Gradien(G2) == -1

# Aplikasi
print (Gradien(MakeGaris(MakePoint(3, 6),MakePoint(2, 4))))

print (PanjangGaris(MakeGaris(MakePoint(3,5), MakePoint(6,3))))

print (TitikPotongX(MakeGaris(MakePoint(2,-2), MakePoint(4,2))))

print (TitikPotongY(MakeGaris(MakePoint(2,-2), MakePoint(4,2))))

print (IsSejajar(MakeGaris(MakePoint(1,2), MakePoint(5,4)), (MakeGaris(MakePoint(1,2), MakePoint(5,4)))))

print (IsTegakLurus(MakeGaris(MakePoint(-1,1), MakePoint(-4,4)), (MakeGaris(MakePoint(1,1), MakePoint(4,4)))))