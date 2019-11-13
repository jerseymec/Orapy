def draw_pattern(n,m):

    for i in range(0,n//2):
        for j in range(0,(m//2)- (i*3+1)):
            print("-", end="")

        for k in range(i*2 +1  ):
            print(".", end="")
            print("|" , end="")
            print(".", end="")

        for j in range(0,(m//2) - (i*3+1)):
            print("-", end="")
        print()
    for l in range ((m//2)-3) :
        print("-", end="")
    print("WELCOME" , end="" )
    for l in range ((m//2)-3) :
        print("-", end="")
    print()
    for i in range(n // 2-1,-1,-1):
        for j in range((m // 2) - (i * 3 + 1),0,-1):
                print("-", end="")

        for k in range(i * 2 + 1):
                print(".", end="")
                print("|", end="")
                print(".", end="")

        for j in range((m // 2) - (i * 3 + 1),0,-1):
                print("-", end="")
        print()
        #print("\n")


draw_pattern(43,129)