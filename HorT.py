import random

Cstring = []
for i in range(101):
   Cstring += random.choice(['H','T'])



print("Head Count: {} ".format(Cstring.count('H')))
print("Tail Count: {} ".format(Cstring.count('T')))
