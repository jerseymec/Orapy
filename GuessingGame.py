import random


secret_num = 7
while True:
    your_num = int (input("Guess the number : "))

    if your_num == secret_num:
        break
    print("Nope not it ")

print("You Guessed it  : ", your_num)
