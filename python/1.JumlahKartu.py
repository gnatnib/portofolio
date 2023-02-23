import ast
lol = ast.literal_eval(input()) 

def islist(s):
    return type(s) == list

kosong = []
def jumlah (x,y):
    for i in (x):
        if islist(i):
            jumlah(i,y)
        else:
            kosong.append(i)

jumlah(lol,kosong)

print (len(kosong))