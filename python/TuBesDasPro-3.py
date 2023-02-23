# Pak Tono mempunyai usaha parkir motor. di pagi hari sudah ada beberapa motor di lahannya yaitu vario-putih, vario-merah, mio-putih, beat-hitam
motor_di_lahan_parkir = ['vario-putih', 'vario-merah', 'mio-putih', 'beat-hitam']
print('Motor di lahan parkir Pak Tono                                                    :', motor_di_lahan_parkir)

# Selang beberapa waktu ada seorang pengendara mio-putih yang parkir di lahan Pak Tono setelah motor tadi
def konsi(S,L):
    if L == []:
        return [S]
    else :
        return L + [S]

motor_di_lahan_parkir_sekarang = konsi('mio-putih', motor_di_lahan_parkir)
print('Motor di lahan parkir Pak Tono setelah kedatangan mio-putih                       :', motor_di_lahan_parkir_sekarang)

# Agar pengendara motor mudah mencari motornya, Pak Tono pun memindahkan motor yang sama jenis dan warnanya ke lahan parkir lain.
def first_element(L):
    return L[0]

def tail(L):
    return L[1:]

def is_empty(L):
    if L == []:
        return True
    else :
        return False

def konso(S,L):
    if L == []:
        return [S]
    else :
        return [S] + L

def is_member(L,x):
    if is_empty(L):
        return False
    else :
        if first_element(L) == x:
            return True
        else :
            return is_member(tail(L), x)

def make_set(L):
    if is_empty(L):
        return []
    else :
        if is_member(tail(L), first_element(L)):
            return make_set(tail(L))
        else :
            return konso(first_element(L), make_set(tail(L)))

motor_di_lahan_parkir_setelah_dipindahkan = make_set(motor_di_lahan_parkir_sekarang)
print('Motor di lahan parkir Pak Tono setelah motor yang sama jenis-warnanya dipindahkan :' , motor_di_lahan_parkir_setelah_dipindahkan)

# Pak Tono memindahkan motor mio-putih ke lahan parkir lain
def konsLi(L,S):
    if L == []:
        return [S]
    else :
        return L + [S]

total_motor = konsLi(motor_di_lahan_parkir_setelah_dipindahkan, ['mio-putih'])
print('Motor di lahan parkir Pak Tono dan lahan parkir lain                              :', total_motor)

# Setelah beberapa hari Pak Tono menggunakan metode memindahlan motor yang sama tipe dan warnanya, ternyata malah banyak pengendara motor yang protes karena kesulitan mencari motor mereka. 
# Akhirnya Pak Tono mempunyai ide dengan setiap tempat motor di lahan parkir diberi nomor yang berurutan, dan setiap pengendara motor akan diberi karcis berisi nomor sesuai tempat parkir motor yang harus ditempati.
class PohonBiner:
    def __init__(self, A, L=None, R=None):
        self.A = A
        self.L = L
        self.R = R
    def __repr__(self):
        return "((%s ,%s), %s" % (repr(self.L), repr(self.A), repr(self.R))

def Akar(P):
    return P.A
def Left(P):
    return P.L
def Right(P):
    return P.R

def MakePB(A, L=None, R=None):
    return PohonBiner(A, L, R)

def IsTreeEmpty(P):
    if P == None:
        return True
    else :
        return False

def IsOneElmt(P):
    if IsTreeEmpty(P):
        return False
    elif IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P)):
        return True
    else :
        return False

def AddX(P, X):
    if IsTreeEmpty(P):
        return MakePB(X)
    elif X > Akar(P):
        return MakePB(Akar(P), Left(P), AddX(Right(P), X))
    elif X < Akar(P):
        return MakePB(Akar(P), AddX(Left(P), X), Right(P))
    else :
        return P

def InOrder(P):
    if IsTreeEmpty(P):
        return []
    elif IsOneElmt(P):
        return [Akar(P)]
    else :
        return InOrder(Left(P)) + [Akar(P)] + InOrder(Right(P))

# Pada suatu hari, datang Andi, Budi, dan Rafli secara berurutan akan parkir di lahan Pak Tono, jika karcis andi bernomor 6, karcis budi bernomor 3, dan karcis rafli bernomor 9, 
# bantu mereka menemukan tempat parkir mereka jika tempat parkir nomor 5 sudah terisi oleh motor Pak Tono!

motor_Pak_Tono = 5
motor_Andi = 6
motor_Budi = 3
motor_Rafli = 9

tempat_parkir = MakePB(motor_Pak_Tono, None, None)

posisi_motor_Andi = InOrder(AddX(tempat_parkir, motor_Andi))
print('Posisi motor Andi di tempat parkir  :', posisi_motor_Andi)
posisi_motor_Budi = InOrder(AddX(AddX(tempat_parkir, motor_Andi), motor_Budi))
print('Posisi motor Budi di tempat parkir  :', posisi_motor_Budi)
posisi_motor_Rafli = InOrder(AddX(AddX(AddX(tempat_parkir, motor_Andi), motor_Budi), motor_Rafli))
print('Posisi motor Rafli di tempat parkir :', posisi_motor_Rafli)

#          T=5
#          /  \
#        B=3  A=6
#              \
#              R=9

#Ket: Left = berada di samping kiri motor
#     Right= berada di samping kanan motor

# Agar posisi motor mereka tidak tertukar, bantu mereka dengan menemukan pemilik motor dan nomor karcisnya!
pemilik_motor = map(lambda x, y : {'Pemilik Motor' : x, 'Nomor Karcis' : y}, ['Budi', 'Pak Tono', 'Andi', 'Rafli'], [3, 5, 6, 9])
print('List Pemilik Motor dan Nomor Karcis :', list(pemilik_motor))