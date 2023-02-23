def konso (s,L):
    if s ==[]:
        return [L]
    else:
        return [s]+L

def konsi(s,L):
    if s ==[]:
        return [L]
    else:
        return L+[s]
        
A = [0,1,2,3]
s = int(input())
p = input()

if p == "konso(s,A)":
    print(konso(s,A))
else:
    print(konsi(s,A))
