tree_height = int(input("Enter the height of the tree : "))
spaces = tree_height - 1
hashes = 1
stump = tree_height - 1
while ( tree_height > 0):

    for i in range (spaces):
        print (' ', end="")
    spaces -=1
    for j in range(hashes) :
        print('#', end="")
    hashes +=2
    print()
    tree_height -=1

for i in range (stump):
    print (' ', end="")
print('#', end="")


