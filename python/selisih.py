def is_member(x,y):
    return x in y

def is_subset(a,b):
    for i in a:
        if not is_member(i,b):
            return False
        return True

def minus(A,B):
    kosong = []
    for i in A:
        if not is_member(i,B):
            kosong.append(i)
    return kosong


A = [5,12, 16, 7, 19, 25, 30]
B = [12, 7, 25]
print (minus(A,B))