# Nested Loops
# Nested loop is a loop inside a loop.

adj = ("red", "big", "tasty")
adj2 = ["good"]
fruits = ("apple", "banana", "cherry")

for x in adj :
    for y in adj2:
        for z in fruits:
            print (x,y,z)