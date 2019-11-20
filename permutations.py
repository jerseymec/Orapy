from itertools import permutations
# Enter your code here. Read input from STDIN. Print output to STDOUT

s, length = input().split()
length = int(length)

permute= list( permutations(sorted(s),length))
#permute.sort()
ab = []
for ab in permute:
    #ab = sorted(a+b)
    print("".join(ab))
#print(permute)

