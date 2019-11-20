from itertools import combinations

s,n = input().split()

for i in range(1,int(n)+1):
    print (*[''.join(a) for a in combinations(sorted(s),i)],sep='\n')