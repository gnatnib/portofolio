# LIST
def jml_element_list(s) :
    return len(s)

def IsList(s) :
    return type(s) == list

def konso(l,s):
    if IsEmpty(s):
        return [l]
    else:
        return [l]+s
    
def konsi(l,s):
    if IsEmpty(s):
        return [l]
    else:
        return s+[l]

def IsEmpty(s) :
    return s == []

def head_list(s) :
    if not IsEmpty(s) :
        return s[1:]

def tail_list(s) :
    if not IsEmpty(s) :
        return s[:-1]

def first_list(s) :
    if not IsEmpty(s) :
        return s[0]

def last_list(s) :
    if not IsEmpty(s) :
        return s[-1]

def IsMember(s1,s2) :
    if IsEmpty(s2) :
        return False
    else :
        if s1 == first_list(s2) :
            return True
        else :
            return IsMember(s1,tail_list(s2))

def IsSubset(s1,s2) :
    if IsEmpty(s1) :
        return True
    else :
        if IsMember(first_list(s1),s2) :
            return IsSubset(tail_list(s1),s2)
        else :
            return False

def IsEq(s1,s2) :
    if len(s1) == len(s2) :
        for i in range(len(s1)) :
            if s1[i] == s2[i] :
                return True

#Set
def IsSet(s) :
    if IsEmpty(s) :
        return True
    else :
        if IsMember(first_list(s),tail_list(s)) :
            return False 
        else :
            return IsSet(tail_list(s))

def MakeSet(s) :
    print(s)
    if IsEmpty(s) :
        return s
    else :
        if IsMember(first_list(s),tail_list(s)) :
            return MakeSet(tail_list(s))
        else :
            return konso(first_list(s),MakeSet(tail_list(s)))

#List Of List 

def IsAtom(s) :
    return not IsEmpty(s) and (jml_element_list(s) == 1)

# CONTOH 1

def IseqL(s1,s2) :
    if IsEmpty(s1) and IsEmpty(s2):
       return True
    elif not IsEmpty(s1) and IsEmpty(s2):
       return False
    elif IsEmpty(s1) and not IsEmpty(s2):
       return False
    else:
        if IsAtom(first_list(s1)) and IsAtom(first_list(s2)):
            if first_list(s1)==first_list(s2) and IseqL(tail_list(s1),tail_list(s2)):
                return True
            else:
                return False
        elif IsList(first_list(s1)) and IsList(first_list(s2)):
            if IseqL(first_list(s1),first_list(s2)) and IseqL(tail_list(s1),tail_list(s2)):
                return True
        else:
            return False

# CONTOH 2
def IsMemberS(A,S) :
    if IsEmpty(S) :
        return False 
    else :
        if IsAtom(first_list(S)):
            if first_list(first_list(S)) == A :
                return True
            else :
                return False
        else :
            if IsMember(A,first_list(S)) :
                return True
            else :
                return IsMemberS(A,tail_list(S))

# CONTOH 3
def IsMemberLS(L,S):
    if IsEmpty(L) and IsEmpty(S):
        return True
    elif not IsEmpty(L) and IsEmpty(S):
        return False
    elif IsEmpty(L) and not IsEmpty(S):
        return False
    else:
        if (IsAtom(first_list(S))):
            IsMemberLS(tail_list(L,S))
        else:
            if IsEq(L,first_list(S)):
                return True
            else:
                IsMemberLS(L,tail_list(S))

# CONTOH 4
def Rember(a,s):
    if IsEmpty(s):
        return s
    else:
        if IsList(first_list(s)):
            konso(Rember(a,first_list(s))), Rember(a,tail_list(s))
        else:
            if first_list(s) == a:
                Rember(a,tail_list(s))
            else:
                konso(first_list(s), Rember(a,tail_list(s)))

# CONTOH 5
def max2(a,b):
    if a>=b:
        return a
    else:
        return b

def Max(S):
    if IsAtom(S):
        if IsAtom(first_list(S)):
            first_list(S)
        else:
            Max(first_list(S))
    else:
        if IsAtom(first_list(S)):
            max2(first_list(S)), Max(tail_list(S))
        else:
            max2(Max(first_list(S))), Max(tail_list(S))
            

L1 = [['a','b','c'],'e',['d','c']]
L2 = [['a'],['q','e']]
L3 = 0
L4 = [1,2,[3,4],5]
L5 = [['a','b'],4,'b']
L6 = [[]]
L7 = [1]
S = [0,1,1,2,3,3,4,5,6,7,8,9]

print (MakeSet(S))
# Bintang Syafrian Rizal - 24060122120031)

        