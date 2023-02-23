import ast
import random
lol = ast.literal_eval(input()) 

def islist(s):
    return type(s)==list
    
y= int(input())

def fungsi(x,y):
    for i in (x):
        if islist(i):
            fungsi(i,y)
        else:
            if i % y == 0:
                x.remove(i)            

for i in range(random.randint(600,650)) :
    fungsi(lol,y)

print(lol)
